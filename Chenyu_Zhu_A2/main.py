"""
Name: Chenyu Zhu
Date:28/01/2023
Brief Project Description: Use kivy to build a reading tracker GUI
GitHub URL:https://github.com/chenyusama/1404/tree/master/Chenyu_Zhu_A2
"""
import os

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.properties import StringProperty

from book import Book
from bookcollection import BookCollection

FILENAME = "books.csv"
KV_FILENAME = "app.kv"
SORT_WAYS = {"Author": "author", "Title": "title", "Pages": "number_of_pages", "Completed": "is_completed"}

GRAY = 0.6, 0.6, 0.6, 1
LIGHT_BLUE = 0.3, 0.6, 0.7, 1


class ReadingTrackerApp(App):
    """ ReadingTrackerApp is a Kivy App for tracking books to read."""
    sort_codes = ListProperty()
    current_sort = StringProperty()
    status_text = StringProperty()
    page_left = StringProperty()

    def __init__(self, **kwargs):
        """Main app."""
        super().__init__(**kwargs)
        self.book_collection = BookCollection()

        # Check if the default file exists and only load the book file if it does.
        if os.path.exists(FILENAME):
            self.book_collection.load_books(FILENAME)
        self.books = self.book_collection.books

    def add_new_book(self, title, author, pages):
        """Add a new book with user entered details and error checking."""
        # Error checking
        if title == "" or title.isspace() or author == "" or author.isspace() or pages == "" or pages.isspace():
            self.status_text = "All fields must be completed"
            return
        if not pages.lstrip("-").isdigit():
            self.status_text = "Please enter a valid number"
            return
        if int(pages) < 1:
            self.status_text = "Pages must be > 0"
            return

        new_book = Book(title, author, int(pages), False)
        self.book_collection.add_book(new_book)
        self.sort_book_widget()
        self.clear_text()

    def display_status_text(self, book):
        """Display a message in the bottom right corner when the book button is pressed."""
        if book.is_completed and book.is_long():
            self.status_text = "You completed {}. Great job!".format(book.title)
        elif book.is_completed:
            self.status_text = "You completed {}.".format(book.title)
        elif book.is_long():
            self.status_text = "You need to read {}. Get started!".format(book.title)
        else:
            self.status_text = "You need to read {}.".format(book.title)

    def initialize_status_text(self):
        """Initializes the status text displayed in the lower right corner."""
        if os.path.exists(FILENAME):
            # Normal welcome message when default file exist
            self.status_text = "Welcome to Reading Tracker 2.0."
        else:
            # Show warning message when default file does not exist
            self.status_text = f"Welcome to Reading Tracker 2.0. Unable to load {FILENAME}!"

    def on_stop(self):
        """Runs when the application exits to save book information to a file."""
        self.book_collection.save_books(FILENAME)

    def create_widgets(self):
        """Create buttons from book list and add them to the GUI."""
        for book in self.books:
            # Create a button for each Book object, specifying the text and background color
            temp_button = Button(text=str(book), background_color=GRAY if book.is_completed else LIGHT_BLUE)
            temp_button.bind(on_release=self.handle_press_book_button)
            # Store a reference to the Book object in the button object
            temp_button.book = book
            self.root.ids.book_button_box.add_widget(temp_button)
        self.display_page_left()

    def handle_press_book_button(self, instance):
        """Handles pressing the book button, changing the state of the book and displaying a message in the bottom
        right corner. """
        book = instance.book
        book.is_completed = not book.is_completed
        self.display_page_left()
        self.sort_book_widget()
        self.display_status_text(book)

    def display_page_left(self):
        """Displays the number of remaining readable pages in the upper right corner."""
        page_left_to_read = 0
        for book in self.books:
            if not book.is_completed:
                page_left_to_read += book.number_of_pages
        self.page_left = f"Pages to read: {page_left_to_read}"

    def clear_text(self):
        """Clears the text in the input field and the bottom state text."""
        self.root.ids.input_title.text = ""
        self.root.ids.input_author.text = ""
        self.root.ids.input_pages.text = ""
        self.status_text = ""

    def sort_book_widget(self):
        """Sorts the book buttons based on the user's selection in the spinner."""
        self.root.ids.book_button_box.clear_widgets()
        self.book_collection.sort(SORT_WAYS[self.root.ids.sort_selection.text])
        self.create_widgets()

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Reading Tracker 2.0"
        self.root = Builder.load_file(KV_FILENAME)
        self.create_widgets()
        self.initialize_status_text()
        self.sort_codes = list(SORT_WAYS.keys())
        self.current_sort = self.sort_codes[0]
        return self.root


if __name__ == '__main__':
    ReadingTrackerApp().run()

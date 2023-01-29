"""BookCollection class"""
import csv
from operator import attrgetter

from book import Book


class BookCollection:

    def __init__(self):
        self.books = []

    def load_books(self, filename):
        with open(filename, "r") as in_file:
            csv_reader = csv.reader(in_file)
            for row in csv_reader:
                if row[3] == "r":
                    is_completed = False
                else:
                    is_completed = True
                load_book = Book(row[0], row[1], int(row[2]), is_completed)
                self.books.append(load_book)

    def add_book(self, book):
        self.books.append(book)

    def sort(self, sort_key):
        self.books.sort(key=attrgetter(sort_key, "title"))

    def get_required_pages(self):
        required_page = 0
        for book in self.books:
            if not book.is_completed:
                required_page += book.number_of_pages
        return required_page

    def save_books(self, filename):
        book_file = open(filename, "w")
        book_information = ""
        for book in self.books:
            book_information += book.title + "," + book.author + "," + str(book.number_of_pages) + ","
            if book.is_completed:
                book_information += "c\n"
            else:
                book_information += "r\n"
        book_file.write(book_information)
        book_file.close()

    def __str__(self):
        """Return a string representation of a BookCollection object."""
        return_message = f"There are {len(self.books)} books in the collection. They are:"
        for i, book in enumerate(self.books):
            return_message += f"\n{i + 1}. {book}"
        return return_message

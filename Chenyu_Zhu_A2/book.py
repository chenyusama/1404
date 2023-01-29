"""Book class"""


class Book:
    def __init__(self, title=" ", author="", number_of_pages=0, is_completed=False):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.is_completed = is_completed

    def mark_completed(self):
        self.is_completed = True

    def mark_required(self):
        self.is_completed = False

    def is_long(self):
        return self.number_of_pages > 500  # Determine if book is larger than 500 pages

    def handle_state_message(self):
        state_message = ""
        if self.is_completed:
            state_message = "(completed)"
        return state_message

    def __str__(self):
        """Return a string representation of a Book object."""
        return f"{self.title} by {self.author}, {self.number_of_pages} pages {self.handle_state_message()}"
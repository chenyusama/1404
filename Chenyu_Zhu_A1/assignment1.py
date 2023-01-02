"""
Name: Chenyu Zhu
Date started:01/01/2023
GitHub URL: https://github.com/chenyusama/1404/tree/master/Chenyu_Zhu_A1
"""
from operator import itemgetter

MENU = """Menu: 
L - List all books 
A - Add new book 
M - Mark a book as completed 
Q - Quit """

FILENAME = "books.csv"

"""location of file information"""
TITLE = 0
AUTHOR = 1
PAGE = 2
REQUIRE = 3

MINIMUM_PAGE_NUMBER = 0
TYPES_OF_BOOK_DETAIL = 4


def main():
    """Reading  tracker program main body."""
    print("Reading Tracker 1.0 - by Chenyu Zhu")

    book_file = open(FILENAME, "r")
    books = load_book(book_file)
    book_file.close()
    books.sort(key=itemgetter(AUTHOR, TITLE))

    print("{} books loaded".format(len(books)))
    print(MENU)
    option = input(">>> ").upper()

    while option != "Q":
        if option == "L":
            display_book(books)
            display_pages_left_to_read(books)
        elif option == "M":
            if count_required_book(books) == 0:
                print("No required books")
            else:
                display_book(books)
                display_pages_left_to_read(books)
                print("Enter the number of a book to mark as completed")
                marked_book = int(handle_book_number_input(">>>", books))
                mark_book(books, marked_book)
        elif option == "A":
            books.append(get_book())
            display_added_message(books)
        else:
            print("Invalid menu option")
        print(MENU)
        option = input(">>> ").upper()
    print("{} books saved to books.csv".format(len(books)))
    print("So many books, so little time. Frank Zappa")
    save_book_information(books)


def save_book_information(books):
    """Save all book information into file."""
    out_file = open(FILENAME, "w")
    book_information = ""
    for book in range(len(books)):
        books[book][PAGE] = str(books[book][PAGE])
    for book in range(len(books)):
        book_information += ",".join(books[book])
        book_information += "\n"
    out_file.write(book_information)
    out_file.close()


def display_added_message(books):
    """Display book added message."""
    added_book = len(books) - 1
    title = books[added_book][TITLE]
    author = books[added_book][AUTHOR]
    pages = books[added_book][PAGE]
    print("{} by {}, ({} pages) added to Reading Tracker".format(title, author, pages))


def get_book():
    """Get new book details from user."""
    title = handle_text_input("Title:")
    author = handle_text_input("Author:")
    pages = int(handle_page_input("Pages:"))
    return [title, author, pages, "r"]


def handle_page_input(input_name):
    """Handle page input with exception."""
    is_valid_input = False
    input_value = None
    while not is_valid_input:
        try:
            input_value = input(f"{input_name} ")
            if input_value == "":
                raise ValueError
            elif int(input_value) <= MINIMUM_PAGE_NUMBER:
                print("Number must be > 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return input_value


def handle_text_input(input_name):
    """Handle text inputs with exception."""
    is_valid_input = False
    input_value = None
    while not is_valid_input:
        try:
            input_value = input("{}".format(input_name))
            if input_value == "":
                raise ValueError
            is_valid_input = True
        except ValueError:
            print("Input can not be blank")
    return input_value


def mark_book(books, marked_book):
    """Mark a book as completed if it is not completed."""
    if not determine_book_state(books, marked_book - 1):
        print("That book is already completed")
    else:
        books[marked_book - 1][REQUIRE] = "c"
        display_marked_message(books, marked_book)


def display_marked_message(books, marked_book):
    """Display the book is completed after mark the book."""
    print(f"{books[marked_book - 1][TITLE]} by "
          f"{books[marked_book - 1][AUTHOR]} completed!")


def handle_book_number_input(input_name, books):
    """Handle book number input with exception."""
    is_valid_input = False
    input_value = None
    while not is_valid_input:
        try:
            input_value = input(f"{input_name} ")
            if int(input_value) <= 0:
                print("Number must be > 0")
            elif int(input_value) > len(books):
                raise IndexError
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
        except IndexError:
            print("Invalid book number")
    return input_value


def count_required_book(books):
    """Count the number of required books left."""
    required_book = 0
    for book in range(len(books)):
        if determine_book_state(books, book):
            required_book += 1
    return required_book


def count_pages_left(books):
    """Count the number of pages left to read."""
    page_number = 0
    for book in range(len(books)):
        if determine_book_state(books, book):
            page_number += books[book][2]
    return page_number


def display_pages_left_to_read(books):
    """Display number of page and book left to read."""
    page_number = count_pages_left(books)
    required_book = count_required_book(books)
    if required_book > 0:
        print("You need to read {} pages in {} books.".format(page_number, required_book))
    else:
        print("No books left to read. Why not add a new book?")


def display_book(books):
    for book in range(len(books)):
        star = determine_star_state(books, book)
        print(f"{star}{book + 1}. {books[book][TITLE]:<40} by "
              f"{books[book][AUTHOR]:<20} {books[book][PAGE]:>5} pages")


def determine_star_state(books, book_number):
    """Return "*" if the book is required."""
    star = " "
    if determine_book_state(books, book_number):
        star = "*"
    return star


def determine_book_state(books, book_number):
    """Determine whether the book is required."""
    return books[book_number][REQUIRE] == "r"


def load_book(book_file):
    """Load the book details from the file to a list."""
    books = []
    for line in book_file:
        books.append(line.strip().split(","))
    for book in range(len(books)):
        books[book][PAGE] = int(books[book][PAGE])
    return books


if __name__ == '__main__':
    main()

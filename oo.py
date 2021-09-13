"""Skills 2: oo.py

Summary.
"""

##
# Design a Bicycle Class


class Bicycle:
    """A bicycle."""
    wheels = 2
    def __init__(self, manufacturer, color):
        
        self.manufacturer = manufacturer
        self.color = color
    # TODO: replace this with your code


##
# Define a Method for Processing Password Changes


class User:
    """A user who can log in to a website."""

    def __init__(self, username, password):
        """Create a user with the given username and password."""

        self.username = username
        self.password = password

    def process_change_password(self, current_password, new_password):
        """Process a password change."""
        if self.password not in current_password:
            raise ValueError("current_password and password don't match")
        else:
            self.password = new_password
        # TODO: replace this with your code


##
# Implement Library Methods


class Book:
    """A book with a title and author."""

    def __init__(self, title, author):
        """Create a book."""

        self.title = title
        self.author = author
        #book 1 = Book(bible, "jesus")
        #print(book1.title) "bible"
        #print(book1.author) "jesus"


class Library: #doesn't need to inherit from book because everything in book is already availabla
    """A library of books."""

    def __init__(self):
        """Create a library."""
        #use super to get the title and author methods from Book class?
        #super().__init__()
        #should the library be a dictionary of author, title k/v pairs?
        self.books = []
        

    def create_and_add_book(self, title, author):
        """Create a Book and add it to the library's list of books."""
        #take in title and author, instantiate a book
        #use super to get the book class?
        
        book = Book(title, author)
        #add book to the library's list of books
        self.books.append(book)

        # TODO: replace this with your code

    def find_books_by_author(self, author):
        """Return a list of books by the given author."""
        books_by_author = []
        #take in an author and return a list of all books written by that author
        #books_by_author.append(getattr(self, author,[]))
        #super().__init__(self, author)
        for book in self.books:
            if book.author == author:
                books_by_author.append(book)#is asking for the book object, not just the title
        return books_by_author
            # else:
            #     continue
      
        # for item in self.books:
        #     if author in item:
        #         books_by_author.append(item[1:])
        #     else:
        #         continue
        # if author in self.books:
        #    books_by_author.append(self.title)
        # else:
        #     return books_by_author
        
        # for self.book in self.books:
        #     if self.author in self.books:
        #         books_by_author.append(self.title)
        #if no books, return empty list
        
        # TODO: replace this with your code


##
# Subclass Rectangle to Implement Square


class Rectangle:
    """A rectangle."""

    def __init__(self, length, width):
        """Create a rectangle."""

        self.length = length
        self.width = width

    def calculate_area(self):
        """Return the area of the rectangle."""

        return self.length * self.width


class Square(Rectangle):
    """A square."""
    def __init__(self, side):
        self.length = side
        self.width = side
    
    def calculate_area(self):
        if self.length == self.width:
            return self.length * self.width
        else:
            raise ValueError("Invalid square.")
    # TODO: replace this with your code


if __name__ == "__main__":
    import sys
    from pathlib import Path

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        try:
            import pytest

            pytest.main([f"test_{Path(__file__).name}"])
        except ModuleNotFoundError:
            print("Unable to run tests because 'pytest' wasn't found :(")
            print("Run the command below to install pytest:")
            print()
            print("    pip3 install pytest")

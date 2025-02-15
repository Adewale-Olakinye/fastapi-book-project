from enum import Enum
from typing import Dict
from pydantic import BaseModel


class Genre(str, Enum):
    """Book genres."""

    SCI_FI = "Science Fiction"
    FANTASY = "Fantasy"
    HORROR = "Horror"
    MYSTERY = "Mystery"
    ROMANCE = "Romance"
    THRILLER = "Thriller"


class Book(BaseModel):
    """Book schema.

    Args:
        BaseModel (BaseModel): Pydantic base model.
    """

    id: int
    title: str
    author: str
    publication_year: int
    genre: Genre


class InMemoryDB:
    """In-memory database for storing books."""

    def __init__(self):
        self.books: Dict[int, Book] = {}  # Changed OrderedDict to regular Dict

    def get_books(self) -> Dict[int, Book]:
        """Gets all books from database.

        Returns:
            Dict[int, Book]: Dictionary of books.
        """
        return self.books

    def add_book(self, book: Book) -> Book:
        """Adds a book to the database.

        Args:
            book (Book): Book to add.

        Returns:
            Book: Added book.
        """
        self.books[book.id] = book  # Directly add the book
        return book  # Ensure the method returns the added book

    def get_book(self, book_id: int) -> Book | None:
        """Gets a specific book from the database.

        Args:
            book_id (int): Book ID.

        Returns:
            Book | None: Book if found, otherwise None.
        """
        return self.books.get(book_id)

    def update_book(self, book_id: int, data: Book) -> Book | None:
        """Updates a specific book in the database.

        Args:
            book_id (int): Book ID.
            data (Book): Updated book data.

        Returns:
            Book | None: Updated book if found, otherwise None.
        """
        if book_id in self.books:
            self.books[book_id] = data
            return data  # Return the updated book
        return None  # Return None if book_id doesn't exist

    def delete_book(self, book_id: int) -> bool:
        """Deletes a specific book from the database.

        Args:
            book_id (int): Book ID.

        Returns:
            bool: True if the book was deleted, False if not found.
        """
        return self.books.pop(book_id, None) is not None  # Return True if deleted, False otherwise


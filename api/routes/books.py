from fastapi import APIRouter, status, HTTPException
from api.db.schemas import Book, Genre

router = APIRouter()

# Ensure db.books is always a dictionary
class InMemoryDB:
    def __init__(self):
        self.books = {}  # Ensures a valid dictionary

# Initialize the database
db = InMemoryDB()
db.books = {
    1: Book(
        id=1,
        title="The Hobbit",
        author="J.R.R. Tolkien",
        publication_year=1937,
        genre=Genre.SCI_FI,
    ),
    2: Book(
        id=2,
        title="1984",
        author="George Orwell",
        publication_year=1949,
        genre=Genre.THRILLER,
    ),
}

@router.get("/api/v1/books/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
def get_book_by_id(book_id: int):
    """
    Retrieve a book by its ID.
    If the book ID does not exist, return a 404 Not Found response.
    """
    if not isinstance(db.books, dict):  # Ensure db.books is a dictionary
        raise HTTPException(status_code=500, detail="Database error: books storage is invalid")

    book = db.books.get(book_id)  # Get the book safely
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book


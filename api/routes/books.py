from typing import Dict
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from api.db.schemas import Book, Genre, InMemoryDB

router = APIRouter()

db = InMemoryDB()
db.books = {
    1: Book(
        id=1,
        title="The Hobbit",
        author="J.R.R. Tolkien",
        publication_year=1937,
        genre=Genre.FANTASY,
    ),
    2: Book(
        id=2,
        title="The Lord of the Rings",
        author="J.R.R. Tolkien",
        publication_year=1954,
        genre=Genre.FANTASY,
    ),
}

@router.get("/api/v1/books", response_model=Dict[int, Book])
def get_books():
    """Retrieve all books."""
    return db.books

@router.get("/api/v1/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    """Retrieve a book by its ID."""
    if book_id not in db.books:
        raise HTTPException(status_code=404, detail="Book not found")
    return db.books[book_id]


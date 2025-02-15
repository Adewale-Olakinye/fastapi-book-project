from fastapi import FastAPI
from api.routes import books  # Import the books router

app = FastAPI()

# Register the books router
app.include_router(books.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Book API"}


from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/books", response_model=list[schemas.BookResponse])
def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def get_the_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book Not Found")
    return book

@app.post("/books", response_model=schemas.BookResponse)
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    new_book = models.Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def change_book_detail(book_id: int, updated_book: schemas.BookCreate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book Not Found")
    
    book.title = updated_book.title
    book.author = updated_book.author
    book.year = updated_book.year
    
    db.commit()
    db.refresh(book)
    return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book Not Found")
    
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}
from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get('/isbn/{isbn}')
async def get_book_by_isbn(isbn: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://openlibrary.org/isbn/{isbn}.json')
    return response.json()

@app.get('/title/{title}')
async def get_book_by_title(title: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'http://openlibrary.org/search.json?title={title}')
    return response.json()['docs'][0]  # Return the first result

@app.get('/author/{author}')
async def get_books_by_author(author: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'http://openlibrary.org/search.json?author={author}')
    return response.json()['docs']  # Return all books by the author

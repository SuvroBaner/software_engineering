from typing import Union
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(title = "The ID of the item to get"),
    q: Union[str, None] = Query(default=None, alias="item-query"),):

    results = {"item_id": item_id}
    if q:
        results.update({'q': q})
    return results

@app.get("/books/{book_id}")
async def read_books(*, book_id: int = Path(title = "The id of the book to get", ge=1), q: int):
    # * : kwargs
    results = {"book_id": book_id}
    if q:
        results.update({"q": q})
    return results



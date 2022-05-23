'''
Query Parameters : When you declare other function parameters that are not part of the path parameters, they are
automatically interpreted as "query" parameters.
'''

from fastapi import FastAPI
from typing import Union

app = FastAPI()

fake_items_db = [{'item_name': "Foo"},
                 {'item_name': "Bar"},
                 {'item_name': "Baz"}]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

# Note: The query is the set of key-value pairs that go after the ? in a URL, separated by & characters

# Optional Params
@app.get("/items/{item_id}")
async def read_item1(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# Multiple path and query parameters 

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item

'''
When you declare a default value for non-path parameters then it is not required.
If you don't want to add a specific value but just make it optional, set the default as None

To make any query parameter required, don't declare any default value -
'''
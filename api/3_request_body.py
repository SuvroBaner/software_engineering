'''
Request Body : This is data sent by the client to your API. The client could be say a browser.
Response Body : The data your API sends to the client.

'''

from typing import Union
from fastapi import FastAPI, Query
from pydantic import BaseModel

'''
Create your own data model which inherits from BaseModel
'''

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()

@app.post('/items/')
async def create_item(item: Item):
    # declare Item as a parameter and add it to your
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

'''
Here FastAPI will read the body of the request as JSON.
'''

# Request body + path + query parameters
@app.put('/items/{item_id}')
async def create_item_full(item_id: int, item: Item, q: Union[str, None] = Query(default=None, min_length=3, max_length=50)):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({'quantity': q})
    return result
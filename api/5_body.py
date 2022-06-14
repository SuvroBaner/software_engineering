'''
Advanced Request Body Declarations
'''

from typing import Union
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(title = 'The ID of the item to get', ge=0, le=1000),
    q: Union[str, None] = None,
    item: Union[Item, None] = None,):

    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    if item:
        results.update({'item_id': item})
    return results

'''
In the above example, the path operations would expect a JSON body with the attributes of an Item
'''

'''
Multiple Body Parameters -
'''

class User(BaseModel):
    username: str
    full_name: Union[str, None] = None

@app.put("/items/{item_id}")
async def update_item2(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results

#### Nested Models #####


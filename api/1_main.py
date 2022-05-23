from lib2to3.pytree import Base
from pyexpat import model
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

'''
Predefined path parameter values
'''

class ModelName(str, Enum):
    # This class inherits from both str and Enum class
    alexnet = 'Alexnet'
    resnet = 'Resnet'
    lenet = 'Lenet'

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name, "item_price": item.price, "is_offer": item.is_offer}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == 'Lenet':
        return {'model_name': model_name, 'message': "LeCNN all the images"}
    
    return {'model_name': model_name, 'message': "Have some residuals"}


# To run it - 
# uvicorn 1_main:app --reload
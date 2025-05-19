from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str #required
    is_done: bool = False

@app.get("/") 
def root():
    return {
        "Hello" : "Worlds"
    }

items = []

@app.post("/items") 
def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items") 
def list_items(limit: int = 10):
    return items[0:limit]

@app.get("/items/{item_id}") 
def get_item(item_id: int) -> Item:
    if(len(items) > 0):
        item = items[item_id]
        return item
    else:
        raise HTTPException(status_code=404, detail=f'Item {item_id} not found')
    

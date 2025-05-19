from fastapi import FastAPI

app = FastAPI()

@app.get("/") 
def root():
    return {
        "Hello" : "World"
    }

items = []

@app.post("/items") 
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items/{item_id}") 
def create_item(item_id: int) -> str:
    item = items[item_id]
    return item
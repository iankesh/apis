from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI() # http://127.0.0.1:8000/docs#/ -> Swagger API

class Item(BaseModel):
	text: str = None
	is_done: bool = False

items = []

@app.get("/")
def root():
	# curl http://127.0.0.1:8000
	return("Hello World")

@app.post("/add-items")
def add_item(item: Item):
	# curl -X POST -H "Content-Type: application/json"  http://127.0.0.1:8000/add-items?item=apple
	items.append(item)
	return items

@app.get("/list-items", response_model=list[Item])
def list_items(limit: int = 10):
	# curl -X GET http://127.0.0.1:8000/list-items
	# curl -X GET http://127.0.0.1:8000/list-items?limit=2
	return items[0:limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
	# curl -X GET http://127.0.0.1:8000/items/1
	if item_id < len(items):
		item = items[item_id]
		return item
	else:
		raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
		




import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/items/")
def read_item_list():
    return {"items": ["item1", "item2", "item3"]}


@app.post("/items/")
def create_item(item: dict):
    return {"item": item}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "item": item}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

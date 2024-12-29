from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def get_product():
    return {"name": "Pop corn"}


@app.get("/item/{items}")
def get_items(items: str, price: int, lotType: str):
    return {"item_name": items, "price": price, "Lot Type": lotType}


@app.get("/test")
def test():
    return {"testing": "completed"}


@app.post("/add/{item}")
def add_item(item: str):
    return {"Added item": item}

import time
from enum import Enum

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Origins that can access the API
origins = [
    # this would be the frontend making requests to the api
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


# python enum to use as fixed values for path parameters
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/users/me")
async def current_user():
    return {"current_user": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# http://127.0.0.1:8000/files/home/user/some.txt
# returns "file_path": "home/user/some.txt"
# http://127.0.0.1:8000/files//home/user/some.txt
# returns "file_path": "/home/user/some.txt"
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# query parameters


fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
]


# http://127.0.0.1:8000/items/?skip=0&limit=10
# http://127.0.0.1:8000/items/
@app.get("/items")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/{item_id}")
async def root(item_id: int):
    return {"item_id": item_id}


@app.post("/items2/")
async def create_item(item: Item):
    return item


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

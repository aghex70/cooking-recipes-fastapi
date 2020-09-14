from fastapi import FastAPI

from routers import recipes

app = FastAPI()

app.include_router(recipes.router)


# from enum import Enum
# from typing import Optional
#
# from fastapi import FastAPI, Query, Path
# from pydantic import BaseModel
#
# from .routers import recipes
#
#
# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#
#
# class User(BaseModel):
#     username: str
#     full_name: Optional[str] = None
#
# # @app.put("/items/{item_id}")
# # async def update_item(item_id: int, item: Item, user: User):
# #     results = {"item_id": item_id, "item": item, "user": user}
# #     return results
# #
# # {
# #     "item": {
# #         "name": "Foo",
# #         "description": "The pretender",
# #         "price": 42.0,
# #         "tax": 3.2
# #     },
# #     "user": {
# #         "username": "dave",
# #         "full_name": "Dave Grohl"
# #     }
# # }
#
#
#
#
# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"
#
#
# app = FastAPI()
#
# app.include_router(
#     recipes.router,
#     prefix="/items",
#     tags=["items"],
#     responses={404: {"description": "Not found"}},
# )
#
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#
#
# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
#     q: Optional[str] = None,
#     item: Optional[Item] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results
#
#
# @app.get("/items/")
# # async def read_items(
# #     q: Optional[str] = Query(
# #         None,
# #         alias="item-query",
# #         title="Query string",
# #         description="Query string for the items to search in the database that have a good match",
# #         min_length=3,
# #         max_length=50,
# #         regex="^fixedquery$",
# #         deprecated=True,
# #     )
# # async def read_items(q: Optional[str] = Query(None, alias="item-query")):
# # async def read_items(
# #     q: Optional[str] = Query(
# #         None,
# #         title="Query string",
# #         description="Query string for the items to search in the database that have a good match",
# #         min_length=3,
# #     )
# # ):
# #async def read_items(q: Optional[List[str]] = Query(None)):
# #async def read_items(q: List[str] = Query(["foo", "bar"])):
# async def read_items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]
#
#
# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict
#
#
# @app.put("/items/{item_id}")
# #async def read_items(q: str = Query("valor por defecto" min_length=3)):  #  lo hace opcional
# #async def read_items(q: str = Query(..., min_length=3)):  #  required usando Query
# async def create_item(item_id: int, item: Item, q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result
#
#
# @router.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id:  int, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:  # != 1, True, true, on, yes
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item
#
#
# @app.get("/itemz/{item_id}")
# async def read_user_item(
#     item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None
# ):
#     item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
#     return item
#
#
# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}
#
#
# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}
#
#
# @app.get("/model/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#
#     return {"model_name": model_name, "message": "Have some residuals"}
#
#
# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}
# """
# You could need the parameter to contain /home/johndoe/myfile.txt, with a leading slash (/).
#
# In that case, the URL would be: /files//home/johndoe/myfile.txt, with a double slash (//) between files and home.
# """

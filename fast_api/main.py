from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

"""
create, read, update, delete

app.post: create
app.get: read
app.put: update
app.delete: delete
"""

items = {
    0 : {"name":"bread",
         "age":1000},
    1: {"name":"water",
        "age":500},
    2: {"name":"라면",
        "age":1200}
}

@app.get("/")
def read_root():
    return {"Hello": "World"}

# path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = items[item_id]
    return item

# path parameter
@app.get("/items/{item_id}/{key}")
def read_item_and_key(item_id: int, key: str):
    item = items[item_id][key]
    return item

# query parameter -> ?로 함. 
@app.get("/item-by-name")
def read_item_by_name(name: str):
    for item_id, item in items.items():
        if item['name'] == name:
            return item
    return {"error":"data not found"}

class ItemForUpdate(BaseModel):
    name: Optional[str]
    price: Optional[int]

class Item(BaseModel):
    name: str
    price: int
    
# pydantic으로 item이 어디서 오는지 정의할 수 있음.. 
# pydantic -> 데이터를 전달할 때 사용하는 라이브러리
# swagger -> UI 로 제공. 
    # 일반적으로 백엔드 개발자가 api를 만듦. 
    # 백엔드보고 프론트엔드 개발자가 application을 만듦.
    # 이 모든 과정을 fastapi 와 swagger로 가능 !!! 
    
@app.post("/items/{item_id}")
def create_item(item_id:int, item: Item):
    if item_id in items:
        return {"error": "there is already existing key."}
    items[item_id] = item.dict()
    return {"sucess":"ok"}

@app.put("/items/{item_id}")
def update_item(item_id:int, item:ItemForUpdate):
    if item_id not in items:
        return {"error": f"there is no item id {item_id}"}
    
    if item.name:
        items[item_id]['name'] = item.name
    
    if item.price:
        items[item_id]['price'] = item.price
        
@app.delete("/item/{item_id}")
def delete_item(item_id:int):
    items.pop(item_id)
    return {"success":"ok"}
    
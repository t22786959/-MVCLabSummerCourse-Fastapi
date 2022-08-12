# FastAPI Tutorial with Basic PyQuery Project
import os
import json
import random
import shutil
from fastapi import FastAPI, HTTPException,File , UploadFile
from fastapi.responses import JSONResponse
from typing import  Union
from pyquery import PyQuery
from pydantic import BaseModel
from uuid import uuid4 # Universally Unique Identifier

# PyDantic BaseModel Class
class Item(BaseModel):
    name: str
    species: str
    gender: str
    age: float

# Exception Class
class MyException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI() # FastAPI Module

# Local data initialize
my_items = []
my_file = 'animals.json'
my_file_names = []
# Load local json file if exist
if os.path.exists(my_file):
    with open(my_file, "r") as f:
        my_items = json.load(f)
        my_items = list(my_items)

# GET Method Exercise (Basic)
@app.get('/')
def root():
    return {"message": "Hello~~  Welcome to  My ZOO!!"}

@app.get('/male-animals')
def male_animals():
    ret=[]
    for i in my_items:
        if i['gender']=='male':
            ret.append(i)
    return ret

@app.get('/all-names')
def all_names():
    ret=[]
    for i in my_items:
        ret.append(i['name'])
    return ret

@app.get('/older-animals')
def older_animals():
    ret=[]
    for i in my_items:
        if i['age']>5:
            ret.append([i['name'],i['age']])
    return ret

@app.get('/delete-lastone')
def or_animals():
    
    my_items.pop()
    return my_items

@app.get('/show-animals')
def show_item():
    if len(my_items):
        return {'Animals':my_items}
    else:
        # Create a exception message
        return {'Item not found'}
        raise HTTPException(404, 'Item not found')



# Exception Handler
@app.exception_handler(MyException)
def call_exception_handler(exc: MyException):
    return JSONResponse (
        status_code= 420,
        content= {
            'Message' : f'Oops ! {exc.name} did something. There goes a rainbow ...'
        }
    )



# POST
@app.post('/add-animal', response_model=Item)
def create_item(item: Item):
    item_dict = item.dict()
    item_dict.update
    my_items.append(item_dict)
    # Save a new item into local database (JSON file)
    with open(my_file, "w") as f:
        json.dump(my_items, f, indent=4)
    return item_dict




# POST 
@app.post('/upload')
def Upload_file(file: Union[UploadFile, None] = None):
    if not file: return {"message" : "No file upload"}
    try:
         file_location = './' + file.filename
         with open(file_location, "wb") as f:
            shutil.copyfileobj(file.file, f)
            file.close()
         my_file_names.append(file.filename)
         return {"Result" : "OK"}
    except:
         raise MyException(name=f'Upload File {file.filename}')


# if __name__ == "__main__"
#     import uvicorn
#     uvicorn.run(app= 'main:app', reload= True) # Default host = 127.0.0.1, port = 8000

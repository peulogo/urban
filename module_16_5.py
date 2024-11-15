from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel
from starlette.templating import Jinja2Templates
from starlette.requests import Request

templates = Jinja2Templates(directory="./templates")
app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, 'users': users})


@app.get('/user/{user_id}')
async def user(request: Request, user_id: int):
    user = next((user for user in users if user.id == user_id), None)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("users.html", {"request": request, "user": user})


@app.post('/users/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(..., title="Enter username", min_length=5, max_length=20, example="UrbanUser")],
        age: Annotated[int, Path(..., title="Enter age", ge=18, le=120, example=24)]
):
    new_user_id = max([user.id for user in users], default=0) + 1
    new_user = User(id=new_user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(..., title="Enter ID")],
        username: Annotated[str, Path(..., title="Enter username", min_length=5, max_length=20, example="UrbanUser")],
        age: Annotated[int, Path(..., title="Enter age", ge=18, le=120, example=24)]
):
    user = next((user for user in users if user.id == user_id), None)

    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    user.username = username
    user.age = age
    return user


@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(..., title="Enter ID")],
):
    user = next((user for user in users if user.id == user_id), None)

    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    users.remove(user)
    return user

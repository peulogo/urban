from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def read_users():
    return users

@app.post('/users/{username}/{age}')
async def create_user(
    username: Annotated[str, Path(..., title="Enter username", min_length=5, max_length=20, example="UrbanUser")],
    age: Annotated[int, Path(..., title="Enter age", ge=18, le=120, example=24)]
):
    new_user_id = int(max(users.keys(), default=0)) + 1
    users[str(new_user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User {new_user_id} is registered"

@app.put('user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[str, Path(..., title="Enter ID")],
        username: Annotated[str, Path(..., title="Enter username", min_length=5, max_length=20, example="UrbanUser")],
        age: Annotated[int, Path(..., title="Enter age", ge=18, le=120, example=24)]
):
    if user_id in users:
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f"User {user_id} is updated"

@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[str, Path(..., title="Enter ID")],
):
    del users[user_id]
    return f'User {user_id} has been deleted'

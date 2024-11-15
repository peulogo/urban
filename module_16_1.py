from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_home():
    return "Главная страница"

@app.get('/user/admin')
def get_user_admin():
    return "Вы вошли как администратор"

@app.get('/user/{user_id}')
def get_user_id(user_id):
    return f"Вы вошли как пользователь № {user_id}"

@app.get('/user')
def get_user_info(username, age):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

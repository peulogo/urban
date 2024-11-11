# Библиотека requests — это инструмент для работы с HTTP-запросами в Python. 
#Она упрощает выполнение запросов, таких как GET, POST, PUT, DELETE и другие, 
#и помогает работать с API, загружать веб-страницы, отправлять данные на сервер и многое другое.

#Get запрос
import requests

# Отправляем GET запрос. Получение данных с веб-страницы или API.
response = requests.get('адрес')

# Проверяем успешность запроса (код 200)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Ошибка при запросе: {response.status_code}")


#Post запрос
# Данные для отправки. Отправка данных на сервер
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправляем POST запрос
response = requests.post('адрес', data=data)

# Проверяем успешность запроса
if response.status_code == 201:
    print("Данные успешно отправлены")
    print(response.json())  # Печатаем ответ сервера
else:
    print(f"Ошибка при отправке данных: {response.status_code}")


#Загрузка файлов
# Скачиваем изображение
url = 'https://optim.tildacdn.com/tild3838-3061-4332-a134-643035333362/-/resize/135x/-/format/webp/Urban_University_log.png'
img_data = requests.get(url).content

# Сохраняем изображение
with open('image.jpg', 'wb') as handler:
    handler.write(img_data)

print("Изображение сохранено как image.jpg")

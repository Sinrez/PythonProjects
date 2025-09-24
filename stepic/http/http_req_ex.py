
# url = 'https://www.example.com/'

import requests
from pprint import pprint

# Пример GET-запроса для получения списка постов
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Проверка статуса и вывод данных
if response.status_code == 200:
    posts = response.json()  # Преобразуем ответ в JSON
    print("GET-запрос успешен! Первый пост:")
    pprint(posts[0])
else:
    print(f"Ошибка: {response.status_code}")


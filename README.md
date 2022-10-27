
# API_Yatube

REST API для социальной сети блогеров Yatube, 

Аутентификация по JWT-токену

Работает со всеми модулями социальной сети Yatube: постами, комментариями, группами, подписчиками


Предоставляет данные в формате JSON
____________________

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/marashka/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

____________________________________

*После запуска сервера полную документацию можно посмотреть по адресу:
http://localhost:8000/redoc/

## Примеры http-запросов
### Пример http-запроса (POST) для создания поста:
```
url = 'http://127.0.0.1/api/v1/posts/'
data = {'text': 'Your post'}
headers = {'Authorization': 'Bearer your_token'}
request = requests.post(url, data=data, headers=headers)
```
### Ответ API_Yatube:
```
Статус- код 200

{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2020-08-20T14:15:22Z"
}
```
_____________________________________________
### Пример http-запроса (GET) для получения списка подписчиков:
```
url = 'http://127.0.0.1:8000/api/v1/follow/'
headers = {'Authorization': 'Bearer your_token'}
request = requests.get(api, headers=headers)
```
### Ответ API_Yatube:
```
Статус- код 200

[
  {
    "user": "string",
    "following": "string"
  }
]
```

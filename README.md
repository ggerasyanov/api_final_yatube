# API для yatube
## Описание проекта.
APi для yatube, это интерфейс для работы с проектом yatube непосредственно через код другой программы. Он выполняет основные функции 
стандартного API. Данная возможность будет очень полезна для других разработчиков, которые хотят общаться с yatube посредством кода)

## Установка
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ggerasyanov/api_final_yatube.git
```

```
cd yatube_api/
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```

## Примеры
Отправив POST запрос на этот эндпоинт можно зарегестрировать аккаунт:
```
http://127.0.0.1:8000/api/v1/jwt/create/
```
Необходимые параметры:
```
{
  "username": "ваше имя",
  "password": "пароль"
}
```
Далее необходимо получить токен для работы с API. GET запросы регестрации не требуют.
Отправте POST Запрос с username и password на эндпоинт:
```
http://127.0.0.1:8000/api/v1/jwt/create/
```
В ответ вы получите токен:
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMDk0MTQ3NywianRpIjoiODUzYzE5MTg5NzMwNDQwNTk1ZjI3ZTBmOTAzZDcxZDEiLCJ1c2VyX2lkIjoxfQ.0vJBPIUZG4MjeU_Q-mhr5Gqjx7sFlO6AShlfeINK8nA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIwODU1Mzc3LCJqdGkiOiJkY2EwNmRiYTEzNWQ0ZjNiODdiZmQ3YzU2Y2ZjNGE0YiIsInVzZXJfaWQiOjF9.eZfkpeNVfKLzBY7U0h5gMdTwUnGP3LjRn5g8EIvWlVg"
} 
```
Запрос к эндпоинту при указанных limit и offset:
```
http://127.0.0.1:8000/api/v1/posts/?limit=1&offset=0
```
Вернёт результат:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
Если нужен результат без пагинации дополнительные параметры можно не указывать.
Можно получить комментарии к посту по этому эндпоинту:
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
Пример ответа:
```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```
Полный перечень возможностей вы можете найти в [документации](http://127.0.0.1:8000/redoc/)

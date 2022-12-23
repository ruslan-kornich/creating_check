## Сервіс генерації чеків
[Тестове завдання](https://docs.google.com/document/d/1Dxp5BM7j3mcQ5lZRRL7yS9orFQypfp4CkozAgYy0PDs/edit) 
## Технічний стек

- Python
- Django
- Docker
- wkhtmltopdf
- PostgreSQL
- Redis

## Install

Встановіть залежності з requirements.txt:
```bash
pip install -r requirements.txt
```
Запустіть docker:
```bash
sudo docker compose up -d --build
```

Застосуйте міграції та створіть суперюзера:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Запустите django-rq в окремому  вiкнi термiналу:
```bash
python manage.py rqworker default
```
Запустіть сервер:
```bash
python manage.py runserver
```
Ендпоінти (на локальній машині)

1. Створення чеків для кухні та для клієнта:

POST: http://127.0.0.1:8000/api/v1/create_checks/

Дані:

```json
{
            "id": "123",
            "price": "1374",
            "items": [
                {
                    "name": "Фiладельфия XXL",
                    "quantity": "1",
                    "unit_price": "899"
                },
                {
                    "name": "Суші з тигровою креветкою",
                    "quantity": "10",
                    "unit_price": "33"
                },
                {
                    "name": "Рамен з беконом XL",
                    "quantity": "1",
                    "unit_price": "145"
                }
            ],
            "address": " вулиця Січеславська Набережна, 39, Дніпро, 49000",
            "client": {
                "name": "Валерiй",
                "phone": "380631234567"
            },
            "point_id": "1"
        }
```

2. Отримання check_id (id чека) за api-key (ключ доступу до принтера):

api_key=key01

http://127.0.0.1:8000/api/v1/new_checks/?api_key=key01

3. Отримання pdf-файлу по api-key та по check_id:

api_key=key01
check_id=1

http://127.0.0.1:8000/api/v1/check/?api_key=key01&check_id=1

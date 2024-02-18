# KokocGroup_test
Тестовое задание для KokocGroup

Сервис для отображения информации о курсе валюты по отношению к рублю на заданную дату
* Стек:
  * Python 3.11
  * Django
  * Celery
  * Redis


## Клонирование проекта
```git clone git@github.com:deepxshine/KokocGroup_test.git```

## Установка зависисостей
```pip install -r requirements.txt```


## Для запуска проекта
Выполните командды:
```bash
  cd kokoc_group 
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver    
```

## Информация о валютах
Что получить дынные по валютам, необходимо выполнить команду:
```python manage.py get_values```
В файле [crontab_example.txt](https://github.com/deepxshine/KokocGroup_test/blob/main/crontab_example.txt) приведен пример contrab команды, котоая запускает команду `python manage.py get_values` каждый день в 7:31


## Дополнительный функционал
В рамках задания настроена Celery-задача, которая раз в день в 04:31 обращается к сервису ЦБ по ардресу: https://www.cbr-xml-daily.ru/daily_json.js

Запуск Celery-задачи:
1) Запуск Redis (Docker)
 ```bash
   docker run -d -p 6379:6379 redis
```
3) Запуск Worker:
 ```bash
celery -A  kokoc_group worker -l info
```
3) Запуск задачи в другом терминале:
 ```bash
   celery -A kokoc_group beat -l info
 ```

## Описание работы
На проекте досупен путь c 2 параметрами: date и charcode. 

http://127.0.0.1:8000/rate/?date="date"&charcode="charcode"

При запросе на этот путь, мы получим данные о курсе указанной валюты по отношению к рублю в указанный день.
### Пример
Запрос:
http://127.0.0.1:8000/rate/?date=2024-02-17&charcode=AED

Ответ:
```{"date": "2024-02-17", "charcode": "AED", "rate": "25.2006"}```

Запрос: 

http://127.0.0.1:8000/rate/?date=2024-02-14&charcode=AED

Ответ

```{"status": "404 Not Found", "detail": "Данные по вашему запросу не найдены"}```

Запрос:

http://127.0.0.1:8000/rate/?date=2024-16-1&charcode=AED

Ответ:

```{"status": "500 Internal Server Error", "detail": "Ошибка обработки запроса.Проверьте правильность введенных данных"}```

Для управления данными досутпна admin-панель

http://127.0.0.1:8000/admin/








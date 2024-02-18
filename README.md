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
В файле [a link]([https://github.com/user/repo/blob/branch/other_file.md](https://github.com/deepxshine/KokocGroup_test/blob/main/crontab_example.txt)) приведен пример contrab команды, котоая запускает команду `python manage.py get_values` каждый день в 7:31


## Дополнительный функционал
В рамках задания настроена Celery-задача, которая раз в день в 04:31 обращается к сервису ЦБ по ардресу: https://www.cbr-xml-daily.ru/daily_json.js

Запуск Celery-задачи:
1) Запуск Redis (Docker)
   ```docker run -d -p 6379:6379 redis```
2) Запуск Worker:
```bash
celery -A  kokoc_group worker -l info
```
3) Запуск задачи в другом терминале:
   ```celery -A kokoc_group beat -l info ```

## На проекте доступен путь:






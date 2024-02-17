import requests
from datetime import datetime

from kokoc_group.celery import app
from .models import Rate

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


@app.task
def get_values():
    json_response = requests.get(URL).json()
    date = json_response['Date']
    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")
    valute = json_response["Valute"]
    keys = valute.keys()
    rates = [Rate(charcode=charcode,
                  date=date,
                  rate=valute[charcode]['Value']) for charcode in keys]
    Rate.objects.bulk_create(rates)
    print(f'Добавленно {len(rates)} новых записей')

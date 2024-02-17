from typing import Any
import requests
from datetime import datetime

from django.core.management.base import BaseCommand

from rates.models import Rate


class Command(BaseCommand):
    help = 'Получение данных о валютах'
    URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

    def handle(self, *args: Any, **options: Any) -> str | None:
        json_response = requests.get(self.URL).json()
        date = json_response['Date']
        date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")
        valute = json_response["Valute"]
        keys = valute.keys()
        rates = [Rate(charcode=charcode,
                      date=date,
                      rate=valute[charcode]['Value'])
                 for charcode in keys]
        Rate.objects.bulk_create(rates)
        print(f'Добавленно {len(rates)} новых записей')

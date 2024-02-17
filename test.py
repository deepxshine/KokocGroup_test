import requests


URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

json_response = requests.get(URL).json()
date = print(json_response['Date'])
valute = json_response["Valute"]
keys = valute.keys()
for charcode in list(keys):
    print(charcode)
    print(valute[charcode]['Value'])
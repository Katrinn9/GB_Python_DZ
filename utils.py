import requests
from decimal import *

getcontext().prec = 4

def currency_rates(valute):
    valute = valute.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if valute not in response:
        return None

    rub = response[response.find('<Value>', response.find(valute)) + 7:response.find('</Value', response.find(valute))]
    return f"{Decimal(rub.replace(',', '.'))}"


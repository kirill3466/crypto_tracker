from time import sleep
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from celery import shared_task

from .models import CryptoCurrency


def get_currency_data(row):
    cryptocurrency = row.find(
        'span', class_='profile__name'
    ).get_text().strip().replace('\n', '')
    values = row.find_all('div', class_='valuta')
    price = values[0].get_text().strip().replace('\n', '')
    market_cap = values[1].get_text().strip().replace('\n', '')
    change = row.find(
        'div', class_='change'
    ).get_text().strip().replace('\n', '')
    return {
        'cryptocurrency': cryptocurrency,
        'price': price,
        'market_cap': market_cap,
        'change': change,
    }


@shared_task
def get_currency():
    """
    Celery task to get currency data and create an object.
    """
    print('Collecting data + creating an object . . .')
    req = Request(
        'https://coinranking.com',
        headers={
            'User-Agent': (
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                'AppleWebKit/605.1.15 (KHTML, like Gecko) '
                'Version/15.6 Safari/605.1.15'
            )
        }
    )
    html = urlopen(req).read()
    bs = BeautifulSoup(html, 'html.parser')
    rows = bs.find(
        'tbody', class_='table__body'
    ).find_all('tr', class_='table__row')[1:6]

    for row in rows:
        data = get_currency_data(row)
        print(data)
        CryptoCurrency.objects.create(**data)
        sleep(5)


@shared_task
def update_currency():
    print('Updating data . . .')
    req = Request(
        'https://coinranking.com',
        headers={
            'User-Agent': (
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                'AppleWebKit/605.1.15 (KHTML, like Gecko) '
                'Version/15.6 Safari/605.1.15'
            )
        }
    )
    html = urlopen(req).read()
    bs = BeautifulSoup(html, 'html.parser')
    rows = bs.find(
        'tbody', class_='table__body'
    ).find_all('tr', class_='table__row')[1:6]

    for row in rows:
        data = get_currency_data(row)
        print(data)
        CryptoCurrency.objects.filter(
            cryptocurrency=data['cryptocurrency']
        ).update(**data)
        sleep(5)


if not CryptoCurrency.objects.exists():
    get_currency()

while True:
    sleep(15)
    update_currency()

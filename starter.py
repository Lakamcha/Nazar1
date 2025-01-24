import requests
from bs4 import BeautifulSoup


class CurrencyConverter:
    def __init__(self, exchange_rate):
        self.exchange_rate = exchange_rate

    def convert_to_usd(self, amount):
        return amount / self.exchange_rate


def get_exchange_rate():
    url = 'https://bank.gov.ua/ua/markets/exchangerates'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'class': 'table-striped'})
    rows = table.find_all('tr')

    for row in rows:
        columns = row.find_all('td')
        if len(columns) > 0 and 'USD' in columns[0].text:
            exchange_rate = float(columns[1].text.replace(',', '.'))
            return exchange_rate

    return None


def main():
    exchange_rate = get_exchange_rate()
    if exchange_rate is None:
        print("Не вдалося отримати курс валют.")
        return

    converter = CurrencyConverter(exchange_rate)

    amount = float(input("Введіть кількість вашої валюти: "))

    result = converter.convert_to_usd(amount)

    print(f"Ваша сума в доларах США: {result:.2f} USD")


if __name__ == "__main__":
    main()

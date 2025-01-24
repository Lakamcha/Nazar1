import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime

conn = sqlite3.connect('weather.db')
conn.execute('''
CREATE TABLE IF NOT EXISTS weather (
    date_time TEXT,
    temperature REAL
)
''')
conn.commit()

url = 'https://www.gismeteo.ua/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

temperature = soup.find('span', class_='unit unit_temperature_c').text.strip()
temperature = float(temperature.replace('°', '').strip())

current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

conn.execute('''
INSERT INTO weather (date_time, temperature)
VALUES (?, ?)
''', (current_time, temperature))

conn.commit()

cursor = conn.execute('SELECT * FROM weather')
for row in cursor:
    print(row)

conn.close()

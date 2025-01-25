import requests
from bs4 import BeautifulSoup
import sqlite3


class Database:
    def __init__(self, db_name="urls.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY,
                url TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_url(self, url):
        self.cursor.execute('''
            INSERT INTO urls (url) VALUES (?)
        ''', (url,))
        self.conn.commit()

    def get_all_urls(self):
        self.cursor.execute('SELECT url FROM urls')
        return [row[0] for row in self.cursor.fetchall()]

    def close(self):
        self.conn.close()


class WebParser:
    def __init__(self):
        self.session = requests.Session()

    def fetch_page(self, url):
        try:
            response = self.session.get(url)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Помилка при запиті до {url}, код статусу: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Помилка під час з'єднання з {url}: {e}")
            return None

    def parse_page(self, html, keyword):
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()
        if keyword.lower() in text.lower():
            return True
        return False


class UserInterface:
    def __init__(self):
        pass

    def get_user_input(self):
        keyword = input("Введіть слово для пошуку: ")
        return keyword


class Program:
    def __init__(self):
        self.database = Database()
        self.parser = WebParser()
        self.ui = UserInterface()

    def run(self):
        keyword = self.ui.get_user_input()
        urls = self.database.get_all_urls()

        for url in urls:
            print(f"Перевіряємо сайт: {url}")
            html = self.parser.fetch_page(url)
            if html and self.parser.parse_page(html, keyword):
                print(f"Знайдено слово '{keyword}' на сайті: {url}")
            else:
                print(f"Слово '{keyword}' не знайдено на сайті: {url}")


if __name__ == "__main__":
    program = Program()
    program.run()

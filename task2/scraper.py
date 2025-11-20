import requests
from bs4 import BeautifulSoup
import json
import time

BASE_URL = "http://quotes.toscrape.com"

def get_soup(url: str):
    # Отримуємо і повертаємо об'єкт BeautifulSoup для заданої URL
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")

def scrape_quotes():
    # Парсить усі цитати з усіх сторінок
    page = 1
    quotes = []
    authors_urls = set()

    while True:
        url = f"{BASE_URL}/page/{page}/"
        soup = get_soup(url)

        quote_blocks = soup.find_all("div", class_="quote")
        if not quote_blocks:
            break  # сторінок більше нема

        for q in quote_blocks:
            text = q.find("span", class_="text").get_text(strip=True)
            author = q.find("small", class_="author").text
            tags = [t.text for t in q.find_all("a", class_="tag")]

            # отримуємо URL автора
            author_link = q.find("a")["href"]
            authors_urls.add(BASE_URL + author_link)

            quotes.append({
                "quote": text,
                "author": author,
                "tags": tags
            })
        page += 1
        time.sleep(0.2) # щоб не перевантажувати сервер
    return quotes, authors_urls

def scrape_author(url: str):
    # Парсить інформацію про автора за його URL
    soup = get_soup(url)

    fullname = soup.find("h3", class_="author-title").text.strip()
    born_date = soup.find("span", class_="author-born-date").text.strip()
    born_location = soup.find("span", class_="author-born-location").text.strip()
    description = soup.find("div", class_="author-description").text.strip()

    return {
        "fullname": fullname,
        "born_date": born_date,
        "born_location": born_location,
        "description": description
    }

def scrape_authors(authors_urls: set):
    # Парсить інформацію про всіх авторів 
    authors = []
    for url in authors_urls:
        authors.append(scrape_author(url))
        time.sleep(0.2)
    return authors

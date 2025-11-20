from scraper import scrape_quotes, scrape_authors
from utils import save_json

def main():
    print("Скрапінг цитат")
    quotes, authors_urls = scrape_quotes()
    print(f"Знайдено цитат: {len(quotes)}")
    print(f"Знайдено авторів: {len(authors_urls)}")

    print("Скрапінг авторів")
    authors = scrape_authors(authors_urls)

    print("Збереження JSON файлів")
    save_json("quotes.json", quotes)
    save_json("authors.json", authors)
    print("Створено файли: quotes.json, authors.json")

if __name__ == "__main__":
    main()

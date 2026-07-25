import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

all_books = []

for page_num in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
    print(f"Scraping page: {page_num}")

    response = requests.get(url)
    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.content, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        name = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        stock = book.find("p", class_="instock availability").text.strip()
        link = "https://books.toscrape.com/catalogue/" + book.h3.a["href"]

        all_books.append({
            "Name": name,
            "Price": price,
            "Stock": stock,
            "Link": link
        })

    time.sleep(1)

df = pd.DataFrame(all_books)
df.to_excel("all_books.xlsx", index=False)
print(f"Process completed! Total {len(all_books)} books pulled.")
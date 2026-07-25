# 📚 Web Scraper App Prototype

A Python-based automated web scraping application designed to extract book details across multiple pages from [Books to Scrape](https://books.toscrape.com) and export the dataset into an Excel file.

---

## ✨ Features

- **Multi-page Pagination:** Automatically iterates through up to 50 pages of catalog listings.
- **Data Extraction:** Extracts essential product fields:
  - Book Title
  - Price
  - Availability / Stock Status
  - Direct Product Link
- **Rate-Limiting / Polite Scraping:** Includes a 1-second delay between requests to prevent server overload.
- **Data Export:** Compiles the scraped output into a clean Pandas DataFrame and saves it as `all_books.xlsx`.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.x
- **Libraries:**
  - `requests` (HTTP requests)
  - `beautifulsoup4` (HTML parsing)
  - `pandas` (Data manipulation & Excel export)
  - `openpyxl` (Engine for Excel writing)

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone [https://github.com/exreinkillz/web_scrapping_app.git](https://github.com/exreinkillz/web_scrapping_app.git)
cd web_scrapping_app
```
### 2. Install dependencies
```
pip install requests beautifulsoup4 pandas openpyxl
```
### 3. Run the scraper
```
python main.py
```

---

## 📝 License

This project is open-source and available for educational purposes.

---

# Python Web Scraper

A multi-source Python web scraping project that retrieves the latest headline data from major UK news platforms.
This project demonstrates core concepts such as HTTP requests, HTML parsing, data extraction, and modular scraper architecture.

---

## Features

- Automated retrieval of headline data
- Support for **multiple news sources**
  - BBC News
  - The Guardian UK
- Modular scraping functions (`scrape_bbc()`, `scrape_guardian()`, `scrape_all()`)
- Clean and structured console output
- Error-free BeautifulSoup parsing workflow

---

## Technologies Used

- Python 3
- Requests
- BeautifulSoup (bs4)

---

## How It Works

The scraper consists of three main components:

### `scrape_bbc()`
Fetches and extracts top headlines from BBC News.

### `scrape_guardian()`
Fetches and extracts top headlines from The Guardian UK.

### `scrape_all()`
Runs both scrapers together and prints aggregated results in a clear formatted structure.

---

## Sample Output

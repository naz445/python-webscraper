import requests
from bs4 import BeautifulSoup

def scrape_bbc():
    url = "https://www.bbc.com/news"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    headlines = soup.select("h3")
    result = []
    for h in headlines[:10]:
        text = h.get_text(strip=True)
        if text:
            result.append(text)
    return result


def scrape_guardian():
    url = "https://www.theguardian.com/uk"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    headlines = soup.select("h3")
    result = []
    for h in headlines[:10]:
        text = h.get_text(strip=True)
        if text:
            result.append(text)
    return result


def scrape_all():
    print("Fetching BBC...")
    bbc_news = scrape_bbc()

    print("Fetching Guardian...")
    guardian_news = scrape_guardian()

    print("\n=== BBC Top Headlines ===")
    for item in bbc_news:
        print("-", item)

    print("\n=== Guardian Top Headlines ===")
    for item in guardian_news:
        print("-", item)

scrape_all()

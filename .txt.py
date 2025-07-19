import requests
from bs4 import BeautifulSoup
def get_toi_headlines():
    url = "https://timesofindia.indiatimes.com/briefs"
    headers = {'User-Agent': 'Mozilla/5.0'}
    resp = requests.get(url, headers=headers)

    if resp.status_code != 200:
        print("Failed to retrieve TOI page")
        return

    soup = BeautifulSoup(resp.content, "html.parser")

    headings = soup.find_all("h2")

    print("📰 Top Times of India Headlines:")
    count = 0
    for h in headings:
        text = h.get_text(strip=True)
        if text:
            print(f"{count + 1}. {text}")
            count += 1
        if count >= 10:
            break


if __name__ == "__main__":
    get_toi_headlines()

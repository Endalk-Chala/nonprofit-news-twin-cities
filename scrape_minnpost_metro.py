import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Expanded date range
START_DATE = datetime(2024, 3, 1)
END_DATE = datetime(2024, 12, 31)

# MinnPost Metro section URL
BASE_URL = "https://www.minnpost.com/category/metro/page/"

# List to collect article data
articles = []

# Scrape up to 50 pages
for page in range(1, 51):
    print(f"Scraping page {page}...")
    url = BASE_URL + str(page)
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Failed to fetch page {page}: {e}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    for post in soup.select("article"):
        title_tag = post.select_one("h2 a")
        date_tag = post.select_one("time")

        if not title_tag or not date_tag:
            continue

        title = title_tag.text.strip()
        link = title_tag['href'].strip()
        date_str = date_tag['datetime'].strip()

        try:
            publish_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")
            publish_date = publish_date.replace(tzinfo=None)
        except Exception as e:
            print(f"⚠️ Skipped article due to date parsing error: {e}")
            continue

        if START_DATE <= publish_date <= END_DATE:
            articles.append({
                "title": title,
                "url": link,
                "date": publish_date.date()
            })

# Save results to CSV
df = pd.DataFrame(articles)
df.to_csv("minnpost_metro_mar_to_dec_2024.csv", index=False)
print("\n✅ Done. Metro articles saved to minnpost_metro_mar_to_dec_2024.csv")




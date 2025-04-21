import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from newspaper import Article

# Date range
START_DATE = datetime(2024, 3, 1)
END_DATE = datetime(2024, 12, 31)

BASE_URL = "https://sahanjournal.com/topics/democracy-politics/page/"

articles = []

# Scrape first 10 pages
for page in range(1, 11):
    print(f"Scraping index page {page}...")
    url = BASE_URL + str(page) + "/"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Failed to fetch page {page}: {e}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    posts = soup.select("article")

    for post in posts:
        title_tag = post.select_one("h2 a")
        date_tag = post.select_one("time")

        if not title_tag or not date_tag:
            continue

        title = title_tag.text.strip()
        link = title_tag['href'].strip()
        date_str = date_tag.get("datetime", "").strip()

        try:
            publish_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")
            publish_date = publish_date.replace(tzinfo=None)
        except Exception as e:
            print(f"⚠️ Skipped article due to date parsing error: {e}")
            continue

        if START_DATE <= publish_date <= END_DATE:
            print(f"  ➤ Extracting article: {title}")
            try:
                article = Article(link)
                article.download()
                article.parse()
                full_text = article.text.strip()
                authors = ", ".join(article.authors)
                top_image = article.top_image
            except Exception as e:
                print(f"    ⚠️ Failed to parse article: {e}")
                full_text = ""
                authors = ""
                top_image = ""

            articles.append({
                "title": title,
                "url": link,
                "date": publish_date.date(),
                "authors": authors,
                "top_image": top_image,
                "text": full_text
            })

# Save to CSV
df = pd.DataFrame(articles)
df.to_csv("sahan_democracy_fulltext_mar_to_dec_2024.csv", index=False)
print("\n✅ Done. Articles saved to sahan_democracy_fulltext_mar_to_dec_2024.csv")

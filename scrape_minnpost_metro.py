import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Date range
START_DATE = datetime(2024, 3, 1)
END_DATE = datetime(2024, 12, 31)

# MinnPost Metro section URL
BASE_URL = "https://www.minnpost.com/category/metro/page/"

# List to collect article data
articles = []

# Scrape first 10 pages
for page in range(1, 11):
    print(f"Scraping index page {page}...")
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
            print(f"  ➤ Extracting article: {title}")
            try:
                article_response = requests.get(link, timeout=10)
                article_soup = BeautifulSoup(article_response.text, "html.parser")

                # Try to extract full text
                content_div = article_soup.select_one(".entry-content, .article-content, .c-article__body")
                full_text = content_div.get_text(separator="\n").strip() if content_div else ""

                # Try to extract author name
                author_tag = article_soup.select_one("a[rel='author'], .author-name, .byline__author")
                authors = author_tag.get_text(strip=True) if author_tag else ""

                # Try to extract top image
                image_tag = article_soup.select_one("meta[property='og:image']")
                top_image = image_tag["content"] if image_tag and "content" in image_tag.attrs else ""

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

# Save results to CSV
df = pd.DataFrame(articles)
df.to_csv("minnpost_metro_fulltext_mar_to_dec_2024.csv", index=False)
print("\n✅ Done. Articles saved to minnpost_metro_fulltext_mar_to_dec_2024.csv")






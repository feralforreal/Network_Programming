#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import csv

def get_website_titles(urls):
    titles = []
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                title = soup.title.text.strip() if soup.title else "No title available"
            else:
                title = "ERR"
        except Exception as e:
            title = "ERR"
        titles.append(title)
    return titles

def write_to_csv(urls, titles):
    with open("top_100_websites_titles.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["URL", "Title"])
        for url, title in zip(urls, titles):
            writer.writerow([url, title])

def main():
    # Access the URL and parse the first 100 website URLs
    url = "https://moz.com/top500"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", {"id": "top-500"})
        rows = table.find_all("tr")[1:101]  # Exclude the header row and get only the first 100 rows
        urls = [row.find_all("td")[1].a["href"] for row in rows]
        
        # Get titles of the websites
        titles = get_website_titles(urls)

        # Write URLs and titles to a CSV file
        write_to_csv(urls, titles)
        print("CSV file created successfully.")
    else:
        print("Failed to access the website.")

if __name__ == "__main__":
    main()






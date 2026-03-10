# Scraper.py

import requests
from bs4 import BeautifulSoup
import csv

class Scraper:
    def __init__(self, url_base):
        self.url_base = url_base
        self.livres = []

    def scraper_page(self, page):
        try:
            url = self.url_base.format(page)
            response = requests.get(url)
            if response.status_code != 200:
                return False
            soup = BeautifulSoup(response.text, "html.parser")
            for livre in soup.find_all("article", class_="product_pod"):
                titre = livre.h3.a["title"]
                prix = livre.find("p", class_="price_color").text.strip()
                self.livres.append([titre, prix])
            return True
        except Exception as e:
            print(f"Erreur page {page} : {e}")
            return False

    def sauvegarder(self):
        with open("livres.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Titre", "Prix"])
            writer.writerows(self.livres)
        print(f"{len(self.livres)} livres sauvegardés ✓")

    def lancer(self):
        page = 1
        print("Scraping en cours...")
        while self.scraper_page(page):
            print(f"Page {page} ✓")
            page += 1
        self.sauvegarder()

# Lancer le scraper
scraper = Scraper("https://books.toscrape.com/catalogue/page-{}.html")
scraper.lancer()
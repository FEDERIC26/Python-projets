# Scraper.py

import requests
from bs4 import BeautifulSoup
import csv

url_base = "https://books.toscrape.com/catalogue/page-{}.html"
tous_les_livres = []
page = 1

print("Scraping en cours...")

while True:
    url = url_base.format(page)
    response = requests.get(url)
    
    # Si la page n'existe pas, on arrête
    if response.status_code != 200:
        break
    
    soup = BeautifulSoup(response.text, "html.parser")
    livres = soup.find_all("article", class_="product_pod")
    
    for livre in livres:
        titre = livre.h3.a["title"]
        prix = livre.find("p", class_="price_color").text.strip()
        dispo = livre.find("p", class_="instock availability").text.strip()
        tous_les_livres.append([titre, prix, dispo])
    
    print(f"Page {page} ✓ ({len(livres)} livres)")
    page += 1

# Sauvegarder en CSV
with open("livres.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Titre", "Prix", "Disponibilité"])
    writer.writerows(tous_les_livres)

print(f"\nTerminé ! {len(tous_les_livres)} livres sauvegardés dans livres.csv")
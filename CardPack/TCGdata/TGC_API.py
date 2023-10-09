import requests
import json

response = requests.get("https://api.pokemontcg.io/v2/cards/?q=set.name:Base")

base1cards = response.json()

with open('base1cards.json', "w", encoding='utf-8') as f:
    json.dump(base1cards, f, ensure_ascii=False, indent=4)


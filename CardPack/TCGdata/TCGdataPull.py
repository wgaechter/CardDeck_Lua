from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity

import json

from pokemontcgsdk import RestClient

RestClient.configure('c314fa11-dd78-4e8e-a886-354a04add315')

card = Card.find('xy1-1')

jsonString = json.dumps(card.__dict__)

print(jsonString)

#jsonFile = open("data.json", "w")
#jsonFile.write(jsonString)
#jsonFile.close()









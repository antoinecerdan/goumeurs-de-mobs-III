from armors.helmet import Helmet
from armors.chestplate import Chestplate
from armors.leggings import Leggings
from armors.boots import Boots

import random


# List of helmets for character creation
starter_helmets = [Helmet("Casque de laitier fou", 50, 1, 1, 25, 4, 10), Helmet("Casque du bouffon joyeux", 50, 1, 1, 25, 4, 10), Helmet("Casque de l'oeuf de Pâques géant", 50, 1, 1, 25, 4, 10)] 
# List of chestplate for character creation
starter_chestplate = [Chestplate("Plastron de la tortue ninja", 50, 1, 1, 25, 4, 10), Chestplate("Plastron du gros câlin", 50, 1, 1, 25, 4, 10), Chestplate("Plastron du coeur brisé", 50, 1, 1, 25, 4, 10)]  
# List of leggings for character creation
starter_leggings = [Leggings("Jambières des coups de pied magiques", 50, 1, 1, 25, 4, 10), Leggings("Jambières de la marche sur les nuages", 50, 1, 1, 25, 4, 10), Leggings("Jambières de la danse enflammée", 50, 1, 1, 25, 4, 10)] 
# List of boots for character creation
starter_boots = [Boots("Bottes de la licorne arc-en-ciel", 50, 1, 1, 25, 4, 10), Boots("Bottes de la rapidité foudroyante", 50, 1, 1, 25, 4, 10), Boots("Bottes de l'élégance trébuchante", 50, 1, 1, 25, 4, 10)] 



# Cette fonction renvoie un élément aléatoire d'un ensemble (bundle)
def get_random_gear(bundle):
    return random.choice(bundle)

# Cette fonction retourne une liste de noms de tous les casques de départ disponibles
def get_all_name_helmet_start() -> list[str]:
    list = []
    for x in starter_helmets:
        list.append(x.name)
    return list

# Cette fonction retourne une liste de noms de toutes les plastrons de départ disponibles
def get_all_name_chestplate_start() -> list[str]:
    list = []
    for x in starter_chestplate:
        list.append(x.name)
    return list

# Cette fonction retourne une liste de noms de tous les pantalons de départ disponibles
def get_all_name_leggins_start() -> list[str]:
    list = []
    for x in starter_leggings:
        list.append(x.name)
    return list

# Cette fonction retourne une liste de noms de toutes les bottes de départ disponibles
def get_all_name_boots_start() -> list[str]:
    list = []
    for x in starter_boots:
        list.append(x.name)
    return list


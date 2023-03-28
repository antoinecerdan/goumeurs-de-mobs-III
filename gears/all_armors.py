from armors.helmet import Helmet
from armors.chestplate import Chestplate
from armors.leggings import Leggings
from armors.boots import Boots

import random


# List of helmets for character creation
starter_helmets = [Helmet("Casque de laitier fou", 1, 1, 1, 1, 1, 1), Helmet("Casque du bouffon joyeux", 1, 1, 1, 1, 1, 1), Helmet("Casque de l'oeuf de Pâques géant", 1, 1, 1, 1, 1, 1)] 
# List of chestplate for character creation
starter_chestplate = [Chestplate("Plastron de la tortue ninja", 1, 1, 1, 1, 1, 1), Chestplate("Plastron du gros câlin", 1, 1, 1, 1, 1, 1), Chestplate("Plastron du coeur brisé", 1, 1, 1, 1, 1, 1)]  
# List of leggings for character creation
starter_leggings = [Leggings("Jambières des coups de pied magiques", 1, 1, 1, 1, 1, 1), Leggings("Jambières de la marche sur les nuages", 1, 1, 1, 1, 1, 1), Leggings("Jambières de la danse enflammée", 1, 1, 1, 1, 1, 1)] 
# List of boots for character creation
starter_boots = [Boots("Bottes de la licorne arc-en-ciel", 1, 1, 1, 1, 1, 1), Boots("Bottes de la rapidité foudroyante", 1, 1, 1, 1, 1, 1), Boots("Bottes de l'élégance trébuchante", 1, 1, 1, 1, 1, 1)] 



def get_random_gear(bundle):
    return random.choice(bundle)

def get_all_name_helmet_start() -> list[str]:
    list = []
    for x in starter_helmets:
        list.append(x.name)
    return list

def get_all_name_chestplate_start() -> list[str]:
    list = []
    for x in starter_chestplate:
        list.append(x.name)
    return list

def get_all_name_leggins_start() -> list[str]:
    list = []
    for x in starter_leggings:
        list.append(x.name)
    return list

def get_all_name_boots_start() -> list[str]:
    list = []
    for x in starter_boots:
        list.append(x.name)
    return list

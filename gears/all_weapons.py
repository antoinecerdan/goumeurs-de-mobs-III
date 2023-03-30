from weapons.arc import Arc
from weapons.baton import Baton
from weapons.bouclier import Bouclier
from weapons.hachette import Hachette
from weapons.masse import Masse

import random


# List of bow for archer creation
starter_bow = [Arc("L'arc-en-ciel explosif",10), Arc("Arc de la pluie d'étoiles",10), Arc("Le poisson volant",10), Arc("Le grand serpent de feu",10)] 
# List of staff for mage creation
starter_staff = [Baton("Le bâton du chaos", 10), Baton("Le bâton qui démange", 10), Baton("Le bâton de la cacophonie", 10), Baton("Le bâton de la licorne", 10)]  
# List of shield for tank creation
starter_shield = [Bouclier("Le bouclier miroir", 10), Bouclier("Le parapluie en fonte", 10), Bouclier("Le bouclier végétal", 10), Bouclier("Le bouclier de l'escargot", 10)] 
# List of hatchet for barbarian creation
starter_hatchet = [Hachette("La hache de l'absurde", 10), Hachette("La hache végane", 10), Hachette("Le couteau à beurre géant", 10), Hachette("La hache qui parle", 10)] 
# List of mass for tank creation
starter_mass = [Masse("Le Fléau du Fromage Fondant", 10), Masse("La Foudre Frite", 10), Masse("L'Ouragan des Olives", 10), Masse("Le Tremblement de Terre aux Tomates", 10)]


# La fonction suivante renvoie un élément aléatoire dans une liste donnée
def get_random_gear(bundle):
    return random.choice(bundle)

# Les fonctions suivantes retournent une liste contenant tous les noms des équipements 
# correspondants à leur type d'équipement. Les noms sont extraits à partir de listes d'objets 
# qui possèdent un attribut nom, tel que starter_bow, starter_staff, etc.
def get_all_name_bow_start() -> list[str]:
    list = []
    for x in starter_bow:
        list.append(x.name)
    return list

def get_all_name_staff_start() -> list[str]:
    list = []
    for x in starter_staff:
        list.append(x.name)
    return list

def get_all_name_shield_start() -> list[str]:
    list = []
    for x in starter_shield:
        list.append(x.name)
    return list

def get_all_name_hatchet_start() -> list[str]:
    list = []
    for x in starter_hatchet:
        list.append(x.name)
    return list

def get_all_name_mass_start() -> list[str]:
    list = []
    for x in starter_mass:
        list.append(x.name)
    return list

from weapons.arc import Arc
from weapons.baton import Baton
from weapons.bouclier import Bouclier
from weapons.hachette import Hachette
from weapons.masse import Masse

import random


# List of bow for archer creation
starter_bow = [Arc("L'arc-en-ciel explosif",25), Arc("Arc de la pluie d'étoiles",30), Arc("Le poisson volant",50), Arc("Le grand serpent de feu",40)] 
# List of staff for mage creation
starter_staff = [Baton("Le bâton du chaos", 25), Baton("Le bâton qui démange", 30), Baton("Le bâton de la cacophonie", 50), Baton("Le bâton de la licorne", 40)]  
# List of shield for tank creation
starter_shield = [Bouclier("Le bouclier miroir", 25), Bouclier("Le parapluie en fonte", 30), Bouclier("Le bouclier végétal", 50), Bouclier("Le bouclier de l'escargot", 40)] 
# List of hatchet for barbarian creation
starter_hatchet = [Hachette("La hache de l'absurde", 25), Hachette("La hache végane", 30), Hachette("Le couteau à beurre géant", 50), Hachette("La hache qui parle", 40)] 
# List of mass for tank creation
starter_mass = [Masse("Le Fléau du Fromage Fondant", 25), Masse("La Foudre Frite", 30), Masse("L'Ouragan des Olives", 50), Masse("Le Tremblement de Terre aux Tomates", 40)]


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

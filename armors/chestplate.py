# Importer la classe "Armor" depuis le module "armors.armor"
from armors.armor import Armor

# La classe "Chestplate" hérite de la classe "Armor"
class Chestplate(Armor):
    # La méthode __init__ de la classe "Chestplate" utilise la méthode __init__ de la classe "Armor" pour initialiser les attributs de la classe "Chestplate"
    def __init__(self, name:str, HP:int, mana:int, rage:int, defense:int, crit_rate:float, crit_dmg:float):
        Armor.__init__(self, name, HP, mana, rage, defense, crit_rate, crit_dmg)
from characters.character import Character  # Importation de la classe Character
from weapons.baton import Baton  # Importation de la classe Baton

class Mage(Character):
    def __init__(self, name:str, hp:int = 200, defense:int = 50, mana:int = 100, weapon:Baton = Baton("", 10)):
        Character.__init__(self, name, hp, defense)  # Appel du constructeur de la classe mère
        self.classe_name = "Mage"  # Définition du nom de classe
        self.mana = mana  # Initialisation de la variable de mana
        self.weapon = weapon  # Initialisation de l'arme
        self.basic_hp = 200  # Initialisation de la santé de base
        self.token_limit = (3,0) #MAGICAL / PHYSICAL  # Limite du nombre de jetons de compétences

    def get_weapon(self) -> Baton:  # Définition de la méthode get_weapon
        return self.weapon  # Retourne l'arme actuelle du mage

    def set_weapon(self, weapon:Baton) -> None:  # Définition de la méthode set_weapon
        self.weapon = weapon  # Affecte l'arme donnée au mage


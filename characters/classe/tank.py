from characters.character import Character # Importation de la classe mère Character
from weapons.masse import Masse # Importation de la classe Masse
from weapons.bouclier import Bouclier # Importation de la classe Bouclier

class Tank(Character): # Définition de la classe Tank qui hérite de la classe mère Character
    def __init__(self, name:str, hp:int = 200, defense:int = 100, rage:int = 50, weapon:Masse = Masse("", 10), shield:Bouclier = Bouclier("",10)):
        Character.__init__(self, name, hp, defense) # Appel du constructeur de la classe mère Character
        self.classe_name = "Tank" # Définition du nom de classe
        self.rage = rage # Définition de l'attribut mana
        self.basic_hp = 200 # Initialisation de la santé de base
        self.weapon = weapon # Initialisation de l'arme
        self.shield = shield # Initialisation du bouclier
        self.token_limit = (0,3) #MAGICAL / PHYSICAL  Définition de l'attribut token_limit
    
    def get_weapon(self) -> Masse: # Définition de la méthode get_weapon qui retourne une instance de la classe Masse
        return self.weapon
    
    def set_weapon(self, weapon:Masse) -> None: # Définition de la méthode set_weapon qui modifie l'attribut weapon avec une instance de la classe Masse
        self.weapon = weapon
    
    def get_shield(self) -> Bouclier: # Définition de la méthode get_shield qui retourne une instance de la classe Bouclier
        return self.shield
    
    def set_shield(self, shield:Bouclier) -> None: # Définition de la méthode set_shield qui modifie l'attribut shield avec une instance de la classe Bouclier
        self.shield = shield

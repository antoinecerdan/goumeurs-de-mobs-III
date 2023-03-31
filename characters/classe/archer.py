# Importer la classe "Character" depuis le module "characters.character"
# Importer la classe "Arc" depuis le module "weapons.arc"
from characters.character import Character
from weapons.arc import Arc

# La classe "Archer" hérite de la classe "Character"
class Archer(Character):
    # La méthode __init__ de la classe "Archer" utilise la méthode __init__ de la classe "Character" pour initialiser les attributs de la classe "Archer"
    def __init__(self, name:str, hp:int = 200, defense:int = 50, mana:int = 100, weapon:Arc = Arc("", 10)):
        # Appeler la méthode __init__ de la classe parente "Character" pour initialiser les attributs de la classe "Archer"
        Character.__init__(self, name, hp, defense)
        self.classe_name = "Archer"
        self.mana = mana
        self.basic_hp = 200
        self.weapon = weapon
        self.token_limit = (3,0) #MAGICAL / PHYSICAL 
        self.nbr_arrow = 10
        # TODO arrow_type
        
    # La méthode "get_weapon" retourne l'arme de l'archer
    def get_weapon(self) -> Arc:
        return self.weapon
    
    # La méthode "set_weapon" définit l'arme de l'archer
    def set_weapon(self, weapon:Arc) -> None:
        self.weapon = weapon
    
    # La méthode "get_nbr_arrow" retourne le nombre de flèches restantes de l'archer
    def get_nbr_arrow(self) -> int:
        return self.nbr_arrow
    
    # La méthode "set_nbr_arrow" définit le nombre de flèches restantes de l'archer
    def set_nbr_arrow(self, nbr_arrow) -> None:
        self.nbr_arrow = nbr_arrow

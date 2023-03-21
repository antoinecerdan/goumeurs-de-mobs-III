from characters.character import Character
from weapons.masse import Masse
from weapons.bouclier import Bouclier

class Tank(Character):
    def __init__(self, name:str, HP:int = 200, defense:int = 100, mana:int = 50, weapon:Masse = Masse("", 10), shield:Bouclier = Bouclier("",10)):
        Character.__init__(self, name, HP, defense)
        self.classe_name = "Tank"
        self.mana = mana
        self.basic_hp = 200
        self.weapon = weapon
        self.shield = shield
        self.token_limit = (1,2) #MAGICAL / PHYSICAL 
    
    def get_weapon(self) -> Masse:
        return self.weapon
    
    def set_weapon(self, weapon:Masse) -> None:
        self.weapon = weapon
    
    def get_shield(self) -> Bouclier:
        return self.shield
    
    def set_shield(self, shield:Bouclier) -> None:
        self.shield = shield
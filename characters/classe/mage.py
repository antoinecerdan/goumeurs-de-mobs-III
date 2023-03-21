from characters.character import Character
from weapons.baton import Baton

class Mage(Character):
    def __init__(self, name:str, HP:int = 200, defense:int = 50, mana:int = 100, weapon:Baton = Baton("", 10)):
        Character.__init__(self, name, HP, defense)
        self.classe_name = "Mage"
        self.mana = mana
        self.weapon = weapon
        self.basic_hp = 200
        self.token_limit = (3,0) #MAGICAL / PHYSICAL 
    
    def get_weapon(self) -> Baton:
        return self.weapon
    
    def set_weapon(self, weapon:Baton) -> None:
        self.weapon = weapon

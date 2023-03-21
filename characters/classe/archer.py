from characters.character import Character
from weapons.arc import Arc

class Archer(Character):
    def __init__(self, name:str, HP:int = 200, defense:int = 50, mana:int = 100, weapon:Arc = Arc("", 10)):
        Character.__init__(self, name, HP, defense)
        self.classe_name = "Archer"
        self.mana = mana
        self.basic_hp = 200
        self.weapon = weapon
        self.token_limit = (2,1) #MAGICAL / PHYSICAL 
        self.nbr_arrow = 10
        # TODO arrow_type
    
    def get_weapon(self) -> Arc:
        return self.weapon
    
    def set_weapon(self, weapon:Arc) -> None:
        self.weapon = weapon
    
    def get_nbr_arrow(self) -> int:
        return self.nbr_arrow
    
    def set_nbr_arrow(self, nbr_arrow) -> None:
        self.nbr_arrow = nbr_arrow
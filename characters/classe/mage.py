from characters.character import Character

class Mage(Character):
    def __init__(self, name:str, HP:int = 200, defense:int = 50, mana:int = 100):
        Character.__init__(self, name, HP, defense)
        self.mana = mana
        self.token_limit = (3,0) #MAGICAL / PHYSICAL 
    
    
    def classe_name(self) -> str:
        return "Mage"

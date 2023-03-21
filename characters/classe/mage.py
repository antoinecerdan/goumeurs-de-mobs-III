from characters.character import Character

class Mage(Character):
    def __init__(self, name:str, HP:int = 200, defense:int = 50, mana:int = 100):
        Character.__init__(self, name, HP, defense)
        self.mana = mana
<<<<<<< HEAD
        self.token_limit = (3,0) #MAGICAL / PHYSICAL 
    
    
    def classe_name(self) -> str:
        return "Mage"
=======
        self.classe_name = "Mage"
>>>>>>> 70d45a801a3d81695f21e79a773ccdb3ac3e732e

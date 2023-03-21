from characters.character import Character

class Tank(Character):
    def __init__(self, name:str, HP:int = 200, defense:int = 100, mana:int = 50):
        Character.__init__(self, name, HP, defense)
        self.mana = mana
<<<<<<< HEAD
        self.token_limit = (1,2)
    
    def classe_name(self) -> str:
        return "Tank"
=======
        self.classe_name = "Tank"
>>>>>>> 70d45a801a3d81695f21e79a773ccdb3ac3e732e

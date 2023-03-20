from characters.character import Character

class Tank(Character):
    def __init__(self, name:str, HP:int = 200, defense:int = 100, mana:int = 50):
        Character.__init__(self, name, HP, defense)
        self.mana = mana
from character import Character

class Tank(Character):
    def __init__(self, name:str, HP:int = 1500, defense:int = 100, mana:int = 50):
        Character.__init__(name, HP, defense)
        self.mana = mana
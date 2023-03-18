from character import Character

class Mage(Character):
    def __init__(self, name:str, HP:int = 500, defense:int = 50, mana:int = 100):
        Character.__init__(name, HP, defense)
        self.mana = mana
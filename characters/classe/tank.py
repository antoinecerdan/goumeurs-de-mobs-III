from character import Character

class Tank(Character):
    def __init__(self, name, HP, defense, mana):
        Character.__init__(name, HP, defense)
        self.mana = mana
from character import Character

class Mage(Character):
    def __init__(self, name, HP, defense, mana):
        Character.__init__(name, HP, defense)
        self.mana = mana
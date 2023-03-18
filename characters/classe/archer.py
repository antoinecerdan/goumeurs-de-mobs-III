from character import Character

class Archer(Character):
    def __init__(self, name, HP, defense, mana):
        Character.__init__(name, HP, defense)
        self.mana = mana
        # todo arrow_nbr
        # todo arrow_type
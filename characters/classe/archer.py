from character import Character

class Archer(Character):
    def __init__(self, name:str, HP:int = 500, defense:int = 50, mana:int = 100):
        Character.__init__(name, HP, defense)
        self.mana = mana
        # todo arrow_nbr
        # todo arrow_type
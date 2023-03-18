from character import Character

class Archer(Character):
    def __init__(self, name:str, HP:int, defense:int, mana:int):
        Character.__init__(name, HP, defense)
        self.mana = mana
        # todo arrow_nbr
        # todo arrow_type
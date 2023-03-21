from characters.character import Character

class Archer(Character):
    def __init__(self, name:str, HP:int = 200, defense:int = 50, mana:int = 100):
        Character.__init__(self, name, HP, defense)
        self.classe_name = "Archer"
        self.mana = mana
        self.token_limit = (2,1) #MAGICAL / PHYSICAL 
        # todo arrow_nbr
        # todo arrow_type
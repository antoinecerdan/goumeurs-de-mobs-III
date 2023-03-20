from characters.character import Character

class Barbarian(Character):
    def __init__(self,name:str, HP:int = 300, defense:int = 25, rage:int = 100):
        Character.__init__(self, name, HP, defense)
        self.rage = rage
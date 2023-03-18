from character import Character

class Barbarian(Character):
    def __init__(self,name:str, HP:int = 650, defense:int = 50, rage:int = 100):
        Character.__init__(name, HP, defense)
        self.rage = rage
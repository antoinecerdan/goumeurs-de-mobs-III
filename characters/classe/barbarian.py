from character import Character

class Barbarian(Character):
    def __init__(self,name:str, HP:int, defense:int, rage:int):
        Character.__init__(name, HP, defense)
        self.rage = rage
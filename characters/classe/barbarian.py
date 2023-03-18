from character import Character

class Barbarian(Character):
    def __init__(self,name, HP, defense, rage):
        Character.__init__(name, HP, defense)
        self.rage = rage
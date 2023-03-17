from classe import Classe

class Barbarian(Classe):
    def __init__(self,name, HP, defense, rage):
        Classe.__init__(name, HP, defense)
        self.rage = rage
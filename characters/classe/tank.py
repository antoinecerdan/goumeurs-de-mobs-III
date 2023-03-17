from classe import Classe

class Tank(Classe):
    def __init__(self, name, HP, defense, mana):
        Classe.__init__(name, HP, defense)
        self.mana = mana
from armors.armor import Armor

class Leggings(Armor):
    def __init__(self, name:str, HP:int, mana:int, rage:int, defense:int, crit_rate:float, crit_dmg:float):
        Armor.__init__(self, name, HP, mana, rage, defense, crit_rate, crit_dmg)
from armors.helmets.helmet import Helmet
from armors.chestplates.chestplate import Chestplate
from armors.leggings.leggings import Leggings
from armors.boots.boots import Boots

class Character:
    def __init__(self, name:str, HP:int, defense:int, helmet:'Helmet', chestplate:'Chestplate', leggings:'Leggings', boots:'Boots', weapon1, weapon2):
        self.name = name
        self.HP = HP
        self.defense = defense
        
        self.helmet = helmet
        self.chestplate = chestplate
        self.leggings = leggings
        self.boots = boots
        self.weapon1 = weapon1
        self.weapon2 = weapon2
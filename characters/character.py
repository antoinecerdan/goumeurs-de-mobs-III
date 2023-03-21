from armors.helmets.helmet import Helmet
from armors.chestplates.chestplate import Chestplate
from armors.leggings.leggings import Leggings
from armors.boots.boots import Boots

class Character:
    def __init__(self, name:str, HP:int, defense:int, helmet:'Helmet' = Helmet("",0,0,0,0,0,0), chestplate:'Chestplate' = Chestplate("",0,0,0,0,0,0), leggings:'Leggings' = Leggings("",0,0,0,0,0,0), boots:'Boots' = Boots("",0,0,0,0,0,0)):
        self.name = name
        self.HP = HP
        self.defense = defense
        self.tokens = []
        self.helmet = helmet
        self.chestplate = chestplate
        self.leggings = leggings
        self.boots = boots
    
    # getter method for helmet
    def get_helmet(self) -> Helmet:
        return self.helmet

    # setter method for helmet
    def set_helmet(self, helmet:'Helmet') -> None:
        self.helmet = helmet
        
    # getter method for chestplate
    def get_chestplate(self) -> Chestplate:
        return self.chestplate

    # setter method for chestplate
    def set_chestplate(self, chestplate:'Chestplate') -> None:
        self.chestplate = chestplate
        
    # getter method for leggings
    def get_leggings(self) -> Leggings:
        return self.leggings

    # setter method for leggings
    def set_leggings(self, leggings:'Leggings') -> None:
        self.leggings = leggings
        
    # getter method for boots
    def get_boots(self) -> Boots:
        return self.boots

    # setter method for boots
    def set_boots(self, boots:'Boots') -> None:
        self.boots = boots
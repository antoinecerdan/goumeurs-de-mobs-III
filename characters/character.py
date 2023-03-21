from armors.helmets.helmet import Helmet
from armors.chestplates.chestplate import Chestplate
from armors.leggings.leggings import Leggings
from armors.boots.boots import Boots

from tokens.token import Token
from tokens.physical_token import PhysicalToken
from tokens.magical_token import MagicalToken

from typing import Type

class Character:
    def __init__(self, name:str, HP:int, defense:int, helmet:'Helmet' = Helmet("",0,0,0,0,0,0), chestplate:'Chestplate' = Chestplate("",0,0,0,0,0,0), leggings:'Leggings' = Leggings("",0,0,0,0,0,0), boots:'Boots' = Boots("",0,0,0,0,0,0)):
        self.name = name
        self.HP = HP
        self.defense = defense
        self.tokens = []
        self.token_limit = (0,0)
        self.helmet = helmet
        self.chestplate = chestplate
        self.leggings = leggings
        self.boots = boots
    
    def equip_token(self,token: Type[Token]):
        if token.isinstance(MagicalToken):
            if self.get_token_types()[0] + 1 > self.token_limit[0]:
                print("no.")
        elif token.isinstance(PhysicalToken):
            if self.get_token_types()[1] + 1 > self.token_limit[1]:
                print("no.")
        else: 
            return -1
    def get_tokens(self):
        return self.tokens
    
    def get_token_types(self):
        res = (0,0)
        for token in self.tokens:
            if token.isinstance(MagicalToken):
                res[0] += 1
            elif token.isinstance(PhysicalToken):
                res[1] += 1
        return res

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
    
    def get_max_HP(self) -> float:
        return (self.HP + self.helmet.get_HP() + self.chestplate.get_HP() + self.leggings.get_HP() + self.boots.get_HP())
    
    def get_defense(self) -> float:
        return (self.defense + self.helmet.get_defense() + self.chestplate.get_defense() + self.leggings.get_defense() + self.boots.get_defense())
    
    def get_crit_rate(self) -> float:
        return (self.helmet.get_crit_rate() + self.chestplate.get_crit_rate() + self.leggings.get_crit_rate() + self.boots.get_crit_rate())
    
    def has_crit_rate(self) -> bool:
        if self.get_crit_rate > 0:
            return True
        else:
            return False
    
    def get_crit_dmg(self) -> float:
        return (self.helmet.get_crit_dmg() + self.chestplate.get_crit_dmg() + self.leggings.get_crit_dmg() + self.boots.get_crit_dmg())
    
    def has_crit_dmg(self) -> bool:
        if self.get_crit_dmg > 0:
            return True
        else:
            return False
    
    def __str__(self) -> str:
        text = f"({self.classe_name}) " + self.name +":"
        if self.HP:
            text += f"\r\n  + {self.HP}/{self.get_max_HP()} HP"
        if self.defense:
            text += f"\r\n  + {self.get_defense()} defense"
        if self.has_crit_rate:
            text += f"\r\n  + {self.get_crit_rate()} crit rate"
        if self.has_crit_dmg:
            text += f"\r\n  + {self.get_crit_dmg()} crit damage"
        if hasattr(self, "mana"):
            text += f"\r\n  + {self.mana} mana"
        if hasattr(self, "rage"):
            text += f"\r\n  + {self.rage} rage"
        return text
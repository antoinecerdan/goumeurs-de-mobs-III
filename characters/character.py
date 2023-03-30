from armors.helmet import Helmet
from armors.chestplate import Chestplate
from armors.leggings import Leggings
from armors.boots import Boots
from math import ceil
import random

from tokens.token import Token
from tokens.physical_token import PhysicalToken
from tokens.magical_token import MagicalToken

from typing import Type

class Character:
    def __init__(self, name:str, hp:int, defense:int, helmet:'Helmet' = Helmet("",0,0,0,0,0,0), chestplate:'Chestplate' = Chestplate("",0,0,0,0,0,0), leggings:'Leggings' = Leggings("",0,0,0,0,0,0), boots:'Boots' = Boots("",0,0,0,0,0,0)):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.tokens = []
        self.token_limit = (0,0)
        self.helmet = helmet
        self.chestplate = chestplate
        self.leggings = leggings
        self.boots = boots
    
    def set_token(self,token: Type[Token]):
        if type(token) == MagicalToken:
            if not (self.get_token_types()[0] + 1 > self.token_limit[0]):
                self.tokens.append(token)
            else: print("You have too much Magical tokens equipped !")
        elif type(token) == PhysicalToken:
            if not (self.get_token_types()[1] + 1 > self.token_limit[1]):
                self.tokens.append(token)
            else: print("You have too much Physical tokens equipped !")
        else: 
            print("Unknown error while switching tokens.")

    def get_tokens(self):
        return self.tokens
    
    def print_tokens(self):
        for token in self.tokens:
            print(str(token) + "\n")

    def get_token_types(self):
        magical = 0
        physical = 0
        for token in self.tokens:
            if type(token) == MagicalToken:
                    magical += 1
            elif type(token) == PhysicalToken:
                physical += 1
        return (magical,physical)

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
    
    def get_max_hp(self) -> float:
        return (self.basic_hp + self.helmet.get_hp() + self.chestplate.get_hp() + self.leggings.get_hp() + self.boots.get_hp())
    
    def get_defense(self) -> float:
        if hasattr(self, "shield"):
            return (self.defense + self.helmet.get_defense() + self.chestplate.get_defense() + self.leggings.get_defense() + self.boots.get_defense()+ self.get_shield().get_defense())
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
    
    def full_heal(self) -> None:
        self.hp = self.get_max_hp()
    
    def is_dead(self) -> bool:
        return self.hp <= 0
    
    def choose_attack(self) -> float:
        choice = None
        while choice not in ['t','h']:
            choice = str(input(f"{self.name}: Do you want to use your [T]okens, or your [H]and weapon ? >>> ")).lower()
        print(choice)
        if choice.lower() == "t":
            return self.launch_tokens()
        if choice.lower() == "h": 
            return self.get_weapon().get_dmg()
    
    def damage_reduction(self, damage, enemy:'Character') -> float:
        defense = enemy.get_defense()
        return ceil((1-(defense/500)) * damage)
    
    def attack(self, damage, enemy:'Character'):
        print(f"{self.name} attacked {enemy.name} and he made {damage} damages")
        enemy.set_damage(damage)
    
    def set_damage(self, damage) -> None:
        hp = self.hp
        self.hp = (hp - damage)
    
    def has_crit(self, damage) -> float:
        if random.random() <= (self.get_crit_rate()/100):
            print("You made a critical move")
            return ceil(damage * (1+(self.get_crit_dmg()/100)))
        return damage
    
    def launch_tokens(self):
        for token in self.get_tokens():
            token.use()
            
    
    def __str__(self) -> str:
        text = f"({self.classe_name}) " + self.name +":"
        if self.hp:
            text += f"\r\n  + {self.hp}/{self.get_max_hp()} hp"
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
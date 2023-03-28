from characters.character import Character
from weapons.hachette import Hachette

class Barbarian(Character):
    def __init__(self,name:str, HP:int = 300, defense:int = 25, rage:int = 100, weapon:Hachette = Hachette("",10)):
        Character.__init__(self, name, HP, defense)
        self.classe_name = "Barbarian"
        self.rage = rage
        self.weapon = weapon
        self.basic_hp = 300
        self.token_limit = (0,3) #MAGICAL / PHYSICAL 
    
    def get_weapon(self) -> Hachette:
        return self.weapon
    
    def set_weapon(self, weapon:Hachette) -> None:
        self.weapon = weapon
        
    def attack(self, damage, enemy:'Character'):
        print(f"{self.name} attacked {enemy.name} and he made {damage} damages")
        enemy.set_damage(damage)
        print(f"{self.name} attacked {enemy.name} and he made {damage} damages")
        enemy.set_damage(damage)

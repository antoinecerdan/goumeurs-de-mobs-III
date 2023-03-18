class Armor:
    def __init__(self, name:str, HP:int, mana:int, rage:int, defense:int, crit_rate:float, crit_dmg:float):
        self.name = name
        self.HP = HP
        self.mana = mana
        self.rage = rage
        self.defense = defense
        self.crit_rate = crit_rate
        self.crit_dmg = crit_dmg
    
    # getter method for HP
    def get_HP(self) -> int:
        return self.HP

    # setter method for HP
    def set_HP(self, HP:int) -> None:
        self.HP = HP
    
    # getter method for mana
    def get_mana(self) -> int:
        return self.mana

    # setter method for mana
    def set_mana(self, mana:int) -> None:
        self.mana = mana
    
    # getter method for rage
    def get_rage(self) -> int:
        return self.rage

    # setter method for rage
    def set_rage(self, rage:int) -> None:
        self.rage = rage
    
    # getter method for defense
    def get_defense(self) -> int:
        return self.defense

    # setter method for defense
    def set_defense(self, defense:int) -> None:
        self.defense = defense
    
    # getter method for crit_rate
    def get_crit_rate(self) -> float:
        return self.crit_rate

    # setter method for crit_rate
    def set_crit_rate(self, crit_rate:float) -> None:
        self.crit_rate = crit_rate
    
    # getter method for crit_dmg
    def get_crit_dmg(self) -> float:
        return self.crit_dmg

    # setter method for crit_dmg
    def set_crit_dmg(self, crit_dmg:float) -> None:
        self.crit_dmg = crit_dmg
    
    def __str__(self) -> str:
        text = self.name +":"
        if self.HP:
            text += f"\r\n  + {self.HP} HP"
        if self.mana:
            text += f"\r\n  + {self.mana} mana"
        if self.rage:
            text += f"\r\n  + {self.rage} rage"
        if self.defense:
            text += f"\r\n  + {self.defense} defense"
        if self.crit_rate:
            text += f"\r\n  + {self.crit_rate} crit rate"
        if self.crit_dmg:
            text += f"\r\n  + {self.crit_dmg} crit damage"
        return text
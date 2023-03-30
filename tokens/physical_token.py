from tokens.token import Token


class PhysicalToken(Token):
    def __init__(self,name:str,damage:int,defense:int,cost:int, trigger_chance:int = 50) -> None:
        super().__init__(name,trigger_chance)
        self.damage = damage
        self.defense = defense
        self.cost = cost

    def attack(self):
        return self.damage




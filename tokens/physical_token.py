from tokens.token import Token


class PhysicalToken(Token):
    def __init__(self,name,damage,defense,trigger_chance) -> None:
        super().__init__(name,trigger_chance)
        self.damage = damage
        self.defense = defense

    def attack():
        return 696969




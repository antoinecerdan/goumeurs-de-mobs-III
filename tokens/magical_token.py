from tokens.token import Token

class MagicalToken(Token):
    def __init__(self,name:str, damage:float, cost:int, trigger_chance:int = 50) -> None:
        super().__init__(name,trigger_chance)
        self.damage = damage
        self.cost = cost

    def attack(self) -> float:
        return self.damage


    def __str__(self) -> str:
        return (f"(MagicalToken) {self.name}\n  + Trigger chance : {self.trigger_chance} %")
        

class Hachette:
    def __init__(self, name:str, damage:int):
        self.name = name
        self.damage = damage
    
    def get_dmg(self) -> int:
        return self.damage
    
    def __str__(self) -> str:
        text = self.name +":"
        if self.damage:
            text += f"\r\n  {self.damage} damage"
        return text
    
    noms_hachettes = ["La hache de l'absurde", 'La hache végane', 'Le couteau à beurre géant', 'La hache qui parle']
class Arc:
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
    
    noms_arcs = ["L'arc-en-ciel explosif", "Arc de la pluie d'étoiles", "Le poisson volant", "Le grand serpent de feu"]
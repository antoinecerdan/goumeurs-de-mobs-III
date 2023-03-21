class Masse:
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
    
    noms_de_masse = ["Le Fléau du Fromage Fondant", "La Foudre Frite", "L'Ouragan des Olives", "Le Tremblement de Terre aux Tomates"]
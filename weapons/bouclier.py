class Bouclier:
    def __init__(self, name:str, defense:int):
        self.name = name
        self.defense = defense
    
    def get_defense(self) -> int:
        return self.defense
    
    def __str__(self) -> str:
        text = self.name +":"
        if self.defense:
            text += f"\r\n  {self.defense} defense"
        return text
    
    noms_boucliers = ['Le bouclier miroir', 'Le parapluie en fonte', 'Le bouclier végétal', "Le bouclier de l'escargot"]
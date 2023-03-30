class Masse:
    def __init__(self, name:str, damage:int):
        # Initialise les attributs "name" et "damage" de la classe Masse
        self.name = name
        self.damage = damage
    
    def get_dmg(self) -> int:
        # Retourne la valeur de l'attribut "damage"
        return self.damage
    
    def __str__(self) -> str:
        # Retourne une chaîne de caractères représentant la masse, y compris son nom et les dégâts infligés
        text = self.name +":"
        if self.damage:
            text += f"\r\n  {self.damage} damage"
        return text
    
    noms_de_masse = ["Le Fléau du Fromage Fondant", "La Foudre Frite", "L'Ouragan des Olives", "Le Tremblement de Terre aux Tomates"]
    # Attribut de classe contenant une liste de noms de masses disponibles

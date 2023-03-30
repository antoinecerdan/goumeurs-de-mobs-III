class Hachette: # Définition de la classe Hachette
    def __init__(self, name:str, damage:int): # Constructeur de la classe qui initialise les attributs name et damage
        self.name = name # Attribut name de l'objet
        self.damage = damage # Attribut damage de l'objet
    
    def get_dmg(self) -> int: # Méthode de la classe qui renvoie les dégâts de l'objet
        return self.damage
    
    def __str__(self) -> str: # Méthode de la classe qui renvoie une chaîne de caractères décrivant l'objet
        text = self.name +":" # Titre de la description
        if self.damage:
            text += f"\r\n  {self.damage} damage" # Description des dégâts si ils sont supérieurs à 0
        return text
    
    noms_hachettes = ["La hache de l'absurde", 'La hache végane', 'Le couteau à beurre géant', 'La hache qui parle'] # Liste des noms possibles des hachettes

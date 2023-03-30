class Bouclier:  # Définition d'une classe Bouclier
    def __init__(self, name:str, defense:int):  # Définition d'une méthode constructeur avec deux paramètres : name et defense
        self.name = name  # Définition d'un attribut nommé name pour l'instance courante
        self.defense = defense  # Définition d'un attribut nommé defense pour l'instance courante
        
    def get_defense(self) -> int:  # Définition d'une méthode appelée get_defense qui retourne un entier
        return self.defense  # Retourne la valeur de l'attribut defense de l'instance courante
    
    def __str__(self) -> str:  # Définition d'une méthode spéciale appelée __str__ qui retourne une chaîne de caractères
        text = self.name +":"  # Définition d'une variable text initialisée avec le nom de l'instance courante et le caractère ":"
        if self.defense:  # Si la valeur de l'attribut defense est différente de 0 (i.e. True)
            text += f"\r\n  {self.defense} defense"  # Ajoute une nouvelle ligne suivie de la valeur de l'attribut defense et du mot "defense" à la variable text
        return text  # Retourne la variable text
    
    noms_boucliers = ['Le bouclier miroir', 'Le parapluie en fonte', 'Le bouclier végétal', "Le bouclier de l'escargot"]  # Définition d'une liste de noms de boucliers qui peut être utilisée par toutes les instances de la classe Bouclier

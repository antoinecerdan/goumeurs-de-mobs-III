class Baton:
    def __init__(self, name:str, damage:int):  # constructeur avec deux attributs : nom et dégâts
        self.name = name
        self.damage = damage
    
    def get_dmg(self) -> int:  # méthode qui retourne les dégâts du bâton
        return self.damage
    
    def __str__(self) -> str:  # méthode qui retourne une chaîne de caractères décrivant le bâton
        text = self.name +":"  # ajoute le nom du bâton
        if self.damage:  # si les dégâts sont non nuls
            text += f"\r\n  {self.damage} damage"  # ajoute la description des dégâts
        return text
    
    noms_batons = ['Le bâton du chaos', 'Le bâton qui démange', 'Le bâton de la cacophonie', 'Le bâton de la licorne']  # liste de noms de bâtons prédéfinis

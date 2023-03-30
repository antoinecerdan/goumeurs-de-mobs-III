# La classe Armor représente une armure dans un jeu ou une simulation
class Armor:
    
    # Le constructeur de la classe. Il est appelé lorsqu'un nouvel objet de la classe est créé.
    # Les paramètres de la méthode correspondent aux attributs de l'objet.
    def __init__(self, name:str, hp:int, mana:int, rage:int, defense:int, crit_rate:float, crit_dmg:float):
        self.name = name # Le nom de l'armure
        self.hp = hp # Les points de vie que l'armure confère
        self.mana = mana # Les points de mana que l'armure confère
        self.rage = rage # Les points de rage que l'armure confère
        self.defense = defense # La quantité de défense que l'armure confère
        self.crit_rate = crit_rate # Le taux de critique que l'armure confère
        self.crit_dmg = crit_dmg # Le multiplicateur de dégâts critiques que l'armure confère

    
    # getter method for HP
    def get_hp(self) -> int:
        return self.hp

    # setter method for HP
    def set_hp(self, hp:int) -> None:
        self.hp = hp
    
    # getter method for mana
    def get_mana(self) -> int:
        return self.mana

    # setter method for mana
    def set_mana(self, mana:int) -> None:
        self.mana = mana
    
    # getter method for rage
    def get_rage(self) -> int:
        return self.rage

    # setter method for rage
    def set_rage(self, rage:int) -> None:
        self.rage = rage
    
    # getter method for defense
    def get_defense(self) -> int:
        return self.defense

    # setter method for defense
    def set_defense(self, defense:int) -> None:
        self.defense = defense
    
    # getter method for crit_rate
    def get_crit_rate(self) -> float:
        return self.crit_rate

    # setter method for crit_rate
    def set_crit_rate(self, crit_rate:float) -> None:
        self.crit_rate = crit_rate
    
    # getter method for crit_dmg
    def get_crit_dmg(self) -> float:
        return self.crit_dmg

    # setter method for crit_dmg
    def set_crit_dmg(self, crit_dmg:float) -> None:
        self.crit_dmg = crit_dmg
    
    # La méthode __str__ est appelée lorsqu'un objet de la classe est converti en une chaîne de caractères
    def __str__(self) -> str:
        text = self.name + ":" # La première ligne du texte de l'armure est le nom de l'armure
        
        # Pour chaque attribut de l'armure, si l'attribut a une valeur différente de 0, ajouter une ligne au texte de l'armure
        if self.hp:
            text += f"\r\n  + {self.hp} hp" # Si l'armure confère des points de vie, ajouter une ligne pour les points de vie
        if self.mana:
            text += f"\r\n  + {self.mana} mana" # Si l'armure confère des points de mana, ajouter une ligne pour les points de mana
        if self.rage:
            text += f"\r\n  + {self.rage} rage" # Si l'armure confère des points de rage, ajouter une ligne pour les points de rage
        if self.defense:
            text += f"\r\n  + {self.defense} defense" # Si l'armure confère de la défense, ajouter une ligne pour la défense
        if self.crit_rate:
            text += f"\r\n  + {self.crit_rate} crit rate" # Si l'armure confère un taux de critique, ajouter une ligne pour le taux de critique
        if self.crit_dmg:
            text += f"\r\n  + {self.crit_dmg} crit damage" # Si l'armure confère un multiplicateur de dégâts critiques, ajouter une ligne pour le multiplicateur de dégâts critiques
        
        return text # Retourner le texte de l'armure complet
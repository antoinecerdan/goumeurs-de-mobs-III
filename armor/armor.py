class Armor:
    def __init__(self, name:str, HP:int, mana:int, rage:int, defense:int, crit_rate:float, crit_dmg:float):
        self.name = name
        self.HP = HP
        self.mana = mana
        self.rage = rage
        self.defense = defense
        self.crit_rate = crit_rate
        self.crit_dmg = crit_dmg


# creation of the helmet list
helmets = [Armor("Casque de laitier fou", 1, 1, 1, 1, 1, 1), Armor("Casque du bouffon joyeux", 1, 1, 1, 1, 1, 1), Armor("Casque de l'oeuf de Pâques géant", 1, 1, 1, 1, 1, 1)] 
# creation of the chestplate list
chestplate = [Armor("Plastron de la tortue ninja", 1, 1, 1, 1, 1, 1), Armor("Plastron du gros câlin", 1, 1, 1, 1, 1, 1), Armor("Plastron du coeur brisé", 1, 1, 1, 1, 1, 1)]  
# creation of the leggings list
leggings = [Armor("Jambières des coups de pied magiques", 1, 1, 1, 1, 1, 1), Armor("Jambières de la marche sur les nuages", 1, 1, 1, 1, 1, 1), Armor("Jambières de la danse enflammée", 1, 1, 1, 1, 1, 1)] 
# creation of the boots list
boots = [Armor("Bottes de la licorne arc-en-ciel", 1, 1, 1, 1, 1, 1), Armor("Bottes de la rapidité foudroyante", 1, 1, 1, 1, 1, 1), Armor("Bottes de l'élégance trébuchante", 1, 1, 1, 1, 1, 1)] 
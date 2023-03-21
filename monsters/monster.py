from math import ceil
import random

class Monster:

    def get_random_name() -> str:
        name_of_monster = ['Croco-mignon', 'Four-midiable', 'Drag-usse', 'Chouette-loup-garou', 'Fanto-melon', 'Ours-polaire-nor-mal', 'Chevalier-raté', 'Kangou-rigolo', 'Cacatoès-trophique', 'Diablotin-farceur', 'Piranha-museau', 'Moche-toi', 'Chauve-sourire', 'Poulpe-dingue', 'Vampire-loufoque', 'Zèbre-musclé', 'Gobelin-voyou', 'Pieuvre-de-rire', 'Lutin-tin', 'Chameau-léon', 'Bouffon-de-mer', 'Sardine-folle', 'Cochon-rigolo', 'Gnou-pas-trop-malin', 'Kraken-taquin', 'Limace-craquante', 'Taupe-là', 'Basilic-calin', 'Hérisson-épicé', 'Mandragore-folle', 'Wombat-marrant', 'Gorille-de-folie', 'Chimpanzé-marrant', 'Lapin-maladroit', 'Harpie-mentale', 'Lézard-gicule', 'Castor-ridicule', 'Eléphant-tastic', 'Oursin-piquant', 'Scarabée-licieux', 'Gazelle-moqueuse', 'Lamantin-grotesque', 'Koala-riant', 'Oie-bêta', 'Pingouin-givré', 'Saumon-rigolo', 'Piranha-cirque', 'Souris-burlesque', 'Thon-tonnant', 'Wapiti-ficelle']
        return random.choice(name_of_monster)
    
    def __init__(self, level:int, name:str, HP:int = 100, defense:int = 50):
        self.name = name
        self.level = level
        self.HP = ceil((level/35) * HP)
        self.defense = ceil((level/35) * defense)
    
    def __str__(self):
        text = f"{self.name}:"
        text += f"\r\n  Level: {self.level}"
        text += f"\r\n  HP: {self.HP} HP"
        text += f"\r\n  Defense: {self.defense} defense"
    
    def set_name(self, name:str) -> None:
        self.name = name
    
    def get_name(self) -> str:
        return self.name
    
    def get_HP(self) -> int:
        return self.HP
    
    def set_HP(self, HP:int) -> None:
        self.HP = HP
        
    def get_defense(self) -> int:
        return self.defense
    
    def set_defense(self, defense:int) -> None:
        self.defense = defense
    
    def set_level(self, level:int) -> None:
        self.level = level
        
    def get_level(self) -> int:
        return self.level
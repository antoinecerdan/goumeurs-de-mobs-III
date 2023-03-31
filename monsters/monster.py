import random
from characters.character import Character
from math import ceil
from sty import fg

class Monster(Character):
    # Fonction qui renvoie un nom de monstre au hasard
    def get_random_name() -> str:
        name_of_monster = ['Croco-mignon', 'Four-midiable', 'Drag-usse', 'Chouette-loup-garou', 'Fanto-melon', 'Ours-polaire-nor-mal', 'Chevalier-raté', 'Kangou-rigolo', 'Cacatoès-trophique', 'Diablotin-farceur', 'Piranha-museau', 'Moche-toi', 'Chauve-sourire', 'Poulpe-dingue', 'Vampire-loufoque', 'Zèbre-musclé', 'Gobelin-voyou', 'Pieuvre-de-rire', 'Lutin-tin', 'Chameau-léon', 'Bouffon-de-mer', 'Sardine-folle', 'Cochon-rigolo', 'Gnou-pas-trop-malin', 'Kraken-taquin', 'Limace-craquante', 'Taupe-là', 'Basilic-calin', 'Hérisson-épicé', 'Mandragore-folle', 'Wombat-marrant', 'Gorille-de-folie', 'Chimpanzé-marrant', 'Lapin-maladroit', 'Harpie-mentale', 'Lézard-gicule', 'Castor-ridicule', 'Eléphant-tastic', 'Oursin-piquant', 'Scarabée-licieux', 'Gazelle-moqueuse', 'Lamantin-grotesque', 'Koala-riant', 'Oie-bêta', 'Pingouin-givré', 'Saumon-rigolo', 'Piranha-cirque', 'Souris-burlesque', 'Thon-tonnant', 'Wapiti-ficelle']
        return random.choice(name_of_monster)
    
    # Constructeur de la classe Monster
    def __init__(self, level:int, name:str, hp:int = 500, defense:int = 100, damage:int = 50):
        Character.__init__(self, name, hp, defense)
        self.name = name
        self.level = level
        self.basic_hp = 500 # Initialisation de la santé de base
        # Calcul des points de vie et de défense du monstre en fonction de son niveau
        self.hp = ceil((level/25) * hp)
        self.defense = ceil((level/25) * defense)
        self.damage = ceil((level/25) * damage)
    
    # Méthode pour afficher les caractéristiques du monstre
    def __str__(self) -> str:
        text = f"{self.name}:"
        text += f"\r\n  Level: {self.level}"
        text += f"\r\n  HP: {self.hp} HP"
        text += f"\r\n  Defense: {self.defense} defense"
        return text
    
    # Méthode pour définir le nom du monstre
    def set_name(self, name:str) -> None:
        self.name = name
    
    # Méthode pour obtenir le nom du monstre
    def get_name(self) -> str:
        return self.name
    
    # Méthode pour obtenir les points de vie du monstre
    def get_HP(self) -> int:
        return self.hp
    
    # Méthode pour définir les points de vie du monstre
    def set_HP(self, hp:int) -> None:
        self.hp
    
    def choose_attack(self) -> float:
        return self.damage

    def attack(self, damage: float, enemy:'Character'):
        print(f"{self.name} attacked {enemy.name} and he made {fg.red}{damage} damages{fg.rs}")
        enemy.set_damage(damage)

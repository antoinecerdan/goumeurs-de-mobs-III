from characters.character import Character
from weapons.hachette import Hachette
from sty import fg

# La classe "Barbarian" hérite de la classe "Character"
class Barbarian(Character):
    """
    Attributs:
    - name (str): le nom du personnage.
    - HP (int): les points de vie du personnage.
    - defense (int): la défense du personnage.
    - rage (int): la quantité de rage du personnage.
    - weapon (Hachette): l'arme équipée du personnage.
    - basic_hp (int): les points de vie de base du personnage.
    - token_limit (Tuple[int, int]): la limite de jetons magiques et physiques que le personnage peut avoir.
    """
    def __init__(self,name:str, hp:int = 300, defense:int = 25, rage:int = 100, weapon:Hachette = Hachette("",10)):
        # Appeler la méthode __init__ de la classe parente "Character" pour initialiser les attributs de la classe "Barbarian"
        Character.__init__(self, name, hp, defense)
        self.classe_name = "Barbarian"
        self.rage = rage
        self.weapon = weapon
        self.basic_hp = 300
        self.token_limit = (0,3) #MAGICAL / PHYSICAL 
    
    # La méthode "get_weapon" retourne l'arme du Barbarian
    def get_weapon(self) -> Hachette:
        return self.weapon
    
    # La méthode "set_weapon" définit l'arme du Barbarian
    def set_weapon(self, weapon:Hachette) -> None:
        self.weapon = weapon
        
    def attack(self, damage, enemy:'Character'):
        """
        Attaque un ennemi avec l'arme équipée du personnage.
        
        Paramètres:
        - damage (int): les dégâts infligés à l'ennemi.
        - enemy (Character): l'ennemi à attaquer.
        """
        # Affiche un message d'attaque.
        print(f"{self.name} attacked {enemy.name} and he made {fg.red}{damage} damages{fg.rs}")
        # Inflige les dégâts à l'ennemi.
        enemy.set_damage(damage)
        # Affiche un message de deuxième attaque (spécifique au Barbare).
        print(f"{self.name} attacked {enemy.name} and he made {fg.red}{damage} damages{fg.rs}")
        # Inflige les dégâts à l'ennemi une deuxième fois.
        enemy.set_damage(damage)

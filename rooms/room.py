from monsters.monster import Monster  # import de la classe Monster depuis le module monsters
import random

class Room:
    def __init__(self, difficulty:int, mobs:list[Monster] = []):
        """
        Constructeur de la classe Room

        Parameters:
        difficulty (int): difficulté de la pièce
        mobs (list[Monster]): liste des monstres dans la pièce (par défaut vide)
        """
        self.difficulty = difficulty
        self.mobs = mobs
    
    def __str__(self) -> str:
        """
        Méthode spéciale pour afficher une représentation en chaîne de caractères de l'objet Room
        """
        text = f"room difficulty : {self.difficulty}"
        for x in self.mobs:
            text += f"\r\n  {x.name}:"
            text += f"\r\n    Level: {x.level}"
            text += f"\r\n    HP: {x.HP} HP"
            text += f"\r\n    Defense: {x.defense} defense"
        return text
    
    def generate_room(self, difficulty) -> None:
        """
        Génère une pièce aléatoire avec des monstres en fonction de la difficulté donnée

        Parameters:
        difficulty (int): difficulté de la pièce
        """
        self.difficulty = difficulty
        if difficulty <= 1:
            for i in range(0,2*difficulty):
                self.mobs.append(Monster(random.randrange(1,10*difficulty),Monster.get_random_name()))
        if difficulty == 2:
            for i in range(0,2*difficulty):
                self.mobs.append(Monster(random.randrange(10,10*difficulty),Monster.get_random_name()))
        if difficulty == 3:
            for i in range(0,2*difficulty):
                self.mobs.append(Monster(random.randrange(10,10*difficulty),Monster.get_random_name()))
        if difficulty == 4:
            for i in range(0,2*difficulty):
                self.mobs.append(Monster(random.randrange(10,10*difficulty),Monster.get_random_name()))
        if difficulty >= 5:
            for i in range(0,2*difficulty):
                self.mobs.append(Monster(random.randrange(10,10*difficulty),Monster.get_random_name()))
    
    def get_difficulty(self) -> int:
        """
        Renvoie la difficulté de la pièce
        """
        return self.difficulty
    
    def get_mobs(self) -> list:
        """
        Renvoie la liste des monstres dans la pièce
        """
        return self.mobs

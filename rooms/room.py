from monsters.monster import Monster
import random

class Room:
    def __init__(self, difficulty:int, mobs:list[Monster] = []):
        self.difficulty = difficulty
        self.mobs = mobs
    
    def __str__(self) -> str:
        text = f"room difficulty : {self.difficulty}"
        for x in self.mobs:
            text += f"\r\n  {x.name}:"
            text += f"\r\n    Level: {x.level}"
            text += f"\r\n    HP: {x.HP} HP"
            text += f"\r\n    Defense: {x.defense} defense"
        return text
    
    def generate_room(self, difficulty) -> None:
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
        return self.difficulty
    
    def get_mobs(self) -> list:
        return self.mobs
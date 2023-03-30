import random

class Token:
    def __init__(self,name,trigger_chance,damage) -> None:
        self.name = name
        self.trigger_chance = trigger_chance

    def use(self) -> float:
        rand = random.randint(1,100)
        # print("rand: " + str(rand) + " trigger chance : " + str(self.trigger_chance))
        if rand >= self.trigger_chance:
            print("The token landed on the good side !")
            return self.attack()
        else:
            print("The token landed on the bad side :(")
            return 0


    def attack(self) -> int:
        pass


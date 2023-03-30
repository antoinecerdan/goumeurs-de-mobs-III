import random

class Token:
    def __init__(self,name,trigger_chance) -> None:
        self.name = name
        self.trigger_chance = trigger_chance

    def use(self):
        rand = random.randint(1,100)
        # print("rand: " + str(rand) + " trigger chance : " + str(self.trigger_chance))
        if rand >= self.trigger_chance:
            print("The token landed on the good side !")
            self.attack()
        else:
            print("The token landed on the bad side :(")
            return 0


    def attack(self):
        return 13


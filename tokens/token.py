import random
from sty import fg

class Token:
    def __init__(self,name,trigger_chance) -> None:
        self.name = name
        self.trigger_chance = trigger_chance

    def use() -> bool:
        rand = random.randint(1,100)
        # print("rand: " + str(rand) + " trigger chance : " + str(self.trigger_chance))
        if rand >= 50:
            print(f"{fg.green}The token landed on the good side !{fg.rs}")
            return True
        else:
            print(f"{fg.red}The token landed on the bad side :({fg.rs}")
            return False
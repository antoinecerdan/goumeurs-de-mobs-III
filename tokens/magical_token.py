from tokens.token import Token

class MagicalToken(Token):
    def __init__(self,name,spell,trigger_chance) -> None:
        super().__init__(name,trigger_chance)
        self.spell = spell

    def attack(self):
        match self.spell:
            case "flashSpell":
                self.flashSpell()

    def flashSpell(self):
        pass



    def __str__(self) -> str:
        return (f"(MagicalToken) {self.name}\n  + Trigger chance : {self.trigger_chance} % \n  + Spell : {self.spell}")
        

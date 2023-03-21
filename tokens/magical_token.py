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


biden = MagicalToken("(BIDEN FLASH)","flashSpell",50)
biden.use()
        

from token import Token

class MagicalToken(Token):
    def __init__(self,name,spell,trigger_chance) -> None:
        super().__init__(name,trigger_chance)
        self.spell = spell

    def attack(self):
        match self.spell:
            case "freezeSpell":
                self.freezeSpell()

    def freezeSpell(self):
        pass


freeze = MagicalToken("Le froid mdr","freezeSpell",50)
freeze.use()
        

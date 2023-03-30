class Arc:
    # Constructor method with parameters name and damage
    def __init__(self, name:str, damage:int):
        self.name = name
        self.damage = damage
    
    # Method to return the damage of the Arc object
    def get_dmg(self) -> int:
        return self.damage
    
    # Method to return a string representation of the Arc object
    def __str__(self) -> str:
        # Initialize the text variable with the name of the Arc object
        text = self.name +":"
        # If the damage of the Arc object is not None, add it to the text variable
        if self.damage:
            text += f"\r\n  {self.damage} damage"
        # Return the string representation of the Arc object
        return text
    
    # Class attribute containing a list of arc names
    noms_arcs = ["L'arc-en-ciel explosif", "Arc de la pluie d'étoiles", "Le poisson volant", "Le grand serpent de feu"]

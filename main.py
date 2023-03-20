import pyfiglet
from enum import Enum
from utilities.parser import parse_user_input

from armors.helmets.helmet import Helmet
from armors.chestplates.chestplate import Chestplate
from armors.leggings.leggings import Leggings
from armors.boots.boots import Boots



# List of helmets for character creation
starter_helmets = [Helmet("Casque de laitier fou", 1, 1, 1, 1, 1, 1), Helmet("Casque du bouffon joyeux", 1, 1, 1, 1, 1, 1), Helmet("Casque de l'oeuf de Pâques géant", 1, 1, 1, 1, 1, 1)] 
# List of chestplate for character creation
starter_chestplate = [Chestplate("Plastron de la tortue ninja", 1, 1, 1, 1, 1, 1), Chestplate("Plastron du gros câlin", 1, 1, 1, 1, 1, 1), Chestplate("Plastron du coeur brisé", 1, 1, 1, 1, 1, 1)]  
# List of leggings for character creation
starter_leggings = [Leggings("Jambières des coups de pied magiques", 1, 1, 1, 1, 1, 1), Leggings("Jambières de la marche sur les nuages", 1, 1, 1, 1, 1, 1), Leggings("Jambières de la danse enflammée", 1, 1, 1, 1, 1, 1)] 
# List of boots for character creation
starter_boots = [Boots("Bottes de la licorne arc-en-ciel", 1, 1, 1, 1, 1, 1), Boots("Bottes de la rapidité foudroyante", 1, 1, 1, 1, 1, 1), Boots("Bottes de l'élégance trébuchante", 1, 1, 1, 1, 1, 1)] 

GAME = True

class State(Enum):
    EXPLORE = 1
    FIGHT = 2
    TOWN = 3
    DEAD = 4

state = State.EXPLORE
if state == state.EXPLORE:
    print("yeysyyese")

print(pyfiglet.figlet_format("Goumeurs de mobs III", font = "3-d" ))

def get_user_input(msg):
    return str(input(msg + " >>>"))

def parse_user_input(cmd):
        cmd.strip()
        cmd.lower()
        cmd = cmd.split()
        print(cmd)
        get_action(cmd)

def get_action(cmd):
        print(cmd)
        match cmd[0]:
                case "say":
                        say(cmd[1])

def generate_user_interface():
    pass

def say(msg):
    print(msg)

while GAME:
    generate_user_interface()
    cmd = get_user_input("Tu fais quoi wsh")
    parse_user_input(cmd)

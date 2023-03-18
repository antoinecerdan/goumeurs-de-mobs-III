import pyfiglet
from armors.helmets.helmet import Helmet
from armors.chestplates.chestplate import Chestplate
from armors.leggings.leggings import Leggings
from armors.boots.boots import Boots

print(pyfiglet.figlet_format("Goumeurs de mobs III", font = "3-d" ))


# List of helmets for character creation
starter_helmets = [Helmet("Casque de laitier fou", 1, 1, 1, 1, 1, 1), Helmet("Casque du bouffon joyeux", 1, 1, 1, 1, 1, 1), Helmet("Casque de l'oeuf de Pâques géant", 1, 1, 1, 1, 1, 1)] 
# List of chestplate for character creation
starter_chestplate = [Chestplate("Plastron de la tortue ninja", 1, 1, 1, 1, 1, 1), Chestplate("Plastron du gros câlin", 1, 1, 1, 1, 1, 1), Chestplate("Plastron du coeur brisé", 1, 1, 1, 1, 1, 1)]  
# List of leggings for character creation
starter_leggings = [Leggings("Jambières des coups de pied magiques", 1, 1, 1, 1, 1, 1), Leggings("Jambières de la marche sur les nuages", 1, 1, 1, 1, 1, 1), Leggings("Jambières de la danse enflammée", 1, 1, 1, 1, 1, 1)] 
# List of boots for character creation
starter_boots = [Boots("Bottes de la licorne arc-en-ciel", 1, 1, 1, 1, 1, 1), Boots("Bottes de la rapidité foudroyante", 1, 1, 1, 1, 1, 1), Boots("Bottes de l'élégance trébuchante", 1, 1, 1, 1, 1, 1)] 
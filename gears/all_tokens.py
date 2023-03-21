from tokens.magical_token import MagicalToken
from tokens.physical_token import PhysicalToken
import random

starter_physical_tokens = []
starter_magical_tokens = []

def get_random_gear(bundle):
    return random.choice(bundle)
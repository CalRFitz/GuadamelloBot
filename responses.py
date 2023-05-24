randommsg = ['Interrupting guady, MOO!', 'Hia', 'No', 'Did somebody say guady?', 'No, you are bald.', 'no you leave', 'My name is guady, I am a piggy.', "Has anybody seen that new horror movie, The Bee Movie?\n\nIt's really good I watched it last night"]
import random
from discord import *
def handle_response(message) -> str:
    p_message = message.lower()

    if 'hello' in p_message:
        return 'Hi!'

    if 'hi' in p_message:
        return ':pig:'

    if 'guady' in p_message:
        return 'Hello'

    if 'guadamello' in p_message:
        return 'Hey are you talking about me!?'

    if 'a' in p_message:
        return randommsg[random.randint(0, 7)]

    if 'x' in p_message:
        return randommsg[random.randint(0, 7)]

    if 'y' in p_message:
        return randommsg[random.randint(0, 7)]

    if 'm' in p_message:
        return randommsg[random.randint(0, 7)]
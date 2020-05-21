"""
input: PROGRAM object
output: game.py
"""

import os

from game_helpers import make_block
from astNodes.PROGRAM import PROGRAM
from .initialize_gamefile import initialize_gamefile

def generate_game(program: PROGRAM):

    initialize_gamefile()

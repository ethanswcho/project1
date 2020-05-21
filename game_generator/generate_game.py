"""
input: PROGRAM object
output: game.py
"""

from game_helpers import make_block
from astNodes.PROGRAM import PROGRAM
from .apply_arena import apply_arena

def generate_game(program: PROGRAM):

    arena = program.arena.evaluate()
    
    game = apply_arena(arena)

    

    return game

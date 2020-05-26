"""
input: PROGRAM object
output: game.py
"""

import os
from astNodes.PROGRAM import PROGRAM
from .get_game_code import get_game_code

game_dir = "game.py"


def generate_game(program: PROGRAM):

    # Code required to initialize the game (and arena)
    initialize_game = program.arena.evaluate()

    # List of code to be used after the game has been generated
    other_code = []

    for ms in program.make_statements:
        other_code.append(ms.evaluate())

    for ms in program.modify_statements:
        other_code.append(ms.evaluate(0))

    loop_code = []
    loop_functions = []

    for i in range(len(program.loops)):
        code, func, time = program.loops[i].evaluate(i)
        loop_code.append(code)
        loop_functions.append((func, time))
    
    # Format the list of codes in other_code to fit python syntax
    formatted_code = program.player.evaluate()
    for c in other_code:
        formatted_code = formatted_code + c + "\n"

    formatted_code = formatted_code + generate_loop_calls(loop_functions)

    for l in loop_code:
        formatted_code = formatted_code + l + "\n"

    formatted_code = formatted_code + generate_destroy_func(loop_functions)

    # Check if gamefile exists first. If it does, delete it.
    if os.path.exists(game_dir):
        print("YES!")
        os.remove(game_dir)

    # Initialize gamefile in specified directory above, and write base game
    with open(game_dir, "w") as game_file:
        game_file.write(get_game_code(initialize_game, formatted_code))


def generate_loop_calls(loop_funcs: list):
    loop_calls = ""
    for lf in loop_funcs:
        loop_calls = loop_calls + f"        arcade.schedule({lf[0]}, {lf[1]})" + "\n"
    return loop_calls


def generate_destroy_func(loop_funcs: list):
    """
    Generates function to unschedule all scheduled loops
    """
    destroy_func = f"    def destroy(self):\n"
    if len(loop_funcs) != 0:
        for lf in loop_funcs:
            destroy_func = destroy_func + f"        pyglet.clock.unschedule({lf[0]})" + "\n"
    else:
        destroy_func = destroy_func + "        pass"
    return destroy_func

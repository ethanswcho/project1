"""
Main method of the program
"""
from astNodes.PROGRAM import PROGRAM
from libs.Tokenizer import Tokenizer
from validate import validate
from generate_game import generate_game
import pprint as pp

def main():

    literals = ["arena size", "make a", "called", "destroy", "set", "of", "to", "change", "by", "move", "wait",
                "do every", ":", "end loop", "ms", "block", "goal", "player", "up", "down", "left", "right", "colour",
                "xpos", "ypos", "width", "height", ",", "at", "with size"]

    Tokenizer.make_tokenizer("config.txt", literals)

    program = PROGRAM()
    program.parse()

    

    # TODO
    # generate_game()

    print("If you get this message the code runs!")

    game_data = program.get_data()
    
    pp.pprint(game_data)

"""
def game_data_printer(game_data: dict):
    for k, v in game_data.items():
        print(k)
        print(v)   
"""


def run_game():
    import game
    print("Running generated game...")
    game.main()

if __name__ == "__main__":
    main()
    run_game()

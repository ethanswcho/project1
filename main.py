"""
Main method of the program
"""
from astNodes.PROGRAM import PROGRAM
from libs.tokenizer import Tokenizer
from game_generator.generate_game import generate_game


def main():

    literals = ["arena size", "make a", "called", "destroy", "set", "of", "to", "change", "by", "move", "wait",
                "do every", ":", "end loop", "ms", "block", "goal", "put player", "up", "down", "left", "right",
                "colour", "xpos", "ypos", "width", "height", ",", "at", "with size"]

    Tokenizer.make_tokenizer("config.txt", literals)

    program = PROGRAM()
    program.parse()

    generate_game(program)

    """
    # Make a new file called game.py, and save generated game
    f = open("game.py", "w")
    f.write(game)
    f.close()
    """

def run_game():
    import game
    print("Running generated game...")
    game.main()

if __name__ == "__main__":
    main()
    run_game()

"""
main method of the program
"""
from astNodes.PROGRAM import PROGRAM
from libs.Tokenizer import Tokenizer
from validate import validate
from generate_game import generate_game

from termcolor import colored
import colorama
import sys

def main():

    literals = ["arena size", "make a", "called", "destroy", "set", "of", "to", "change", "by", "move", "wait",
                "do every", ":", "end loop", "ms", "block", "goal", "player", "up", "down", "left", "right", "colour",
                "xpos", "ypos", "width", "height", "#"]

    #Initialize colors
    colorama.init()

    print(colored("Initializing project...", "green"))
    print(colored("Starting tokenizer...", "green"))

    Tokenizer.make_tokenizer("config.txt", literals)

    print (colored("Tokenizing success...", "green"))

    program = PROGRAM()

    print(colored("Starting parser...", "green"))

    parsed_commands = program.parse()

    is_valid, error_notes = validate(parsed_commands)

    if is_valid is False:
        for en in error_notes:
            print(colored(en, "red"))
        
        #TODO: Better error handling here
        #sys.exit()
    
    print(colored("Parsing success...", "green"))

    print(colored("Generating game...", "green"))

    generate_game(parsed_commands)

    print(colored("Generating game success...", "green"))

    import generated_game

    #print("If you get this message the code runs!")

#Imports the generated gamefile (needs to be called generated_game.py), and executes the file's run() method.
def run_game():
    import example_game
    print(colored("Running generated game...", "green"))
    example_game.main()

if __name__ == "__main__":
    main()
    run_game()


"""
sample input:
    "
    make blue block block1 at 20, 40 with 40 width
    do every 10 second: block1 shift right by 5
    do every 10 second: gravity increases by 2
    "
"""
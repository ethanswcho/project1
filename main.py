"""
main method of the program
"""
from astNodes.PROGRAM import PROGRAM
from libs.Tokenizer import Tokenizer
from validate import validate
from generate_game import generate_game


def main():

    literals = ["set arena size:", "make a", "called", "remove", "set", "of", "to", "increase", "decrease", "by",
                "move", "wait", "do every", ":", "end loop", "millisecond", "second", "block", "end block", "player",
                "up", "down", "left", "right", "colour", "xpos", "ypos", "width", "height", "#"]

    Tokenizer.make_tokenizer("config.txt", literals)

    program = PROGRAM()
    parsed_commands = program.parse()

    is_valid, error_notes = validate(parsed_commands)

    if is_valid is False:
        for en in error_notes:
            print(en)
        """
        Error handling (TBD) 
        """

    generate_game(parsed_commands)

    print("If you get this message the code runs!")


if __name__ == "__main__":
    main()


"""
sample input:
    "
    make blue block block1 at 20, 40 with 40 width
    do every 10 second: block1 shift right by 5
    do every 10 second: gravity increases by 2
    "
"""
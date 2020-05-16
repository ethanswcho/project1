"""
main method of the program
"""

from tokenize import tokenize
from parse import parse
from validate import validate
from generate_game import generate_game

def main():

    #Open the file, copy the content, and close
    #The file should be inside same folder as the python scripts (or we can specify the file location here as a global variable)
    f = open("config.txt")
    input_text = f.read()
    f.close()


    tokenized_input = tokenize(input_text)

    parsed_commands = parse(tokenized_input)

    is_valid, error_notes = validate(parsed_commands)

    if is_valid is False:
        for en in error_notes:
            print(error_notes)
        """
        Error handling (TBD) 
        """

    generate_game(parsed_commands)


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
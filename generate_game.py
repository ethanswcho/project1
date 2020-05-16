"""
input: parsed_commands
output: ???
"""

from .game_helpers import make_block

def generate_game(parsed_commands: dict):

    """
    takes in a dictionary of pasred commands, and generate a game using commands and variables contained within.
    commands (keys of the parsed_commands dictionary) should be used to determine which helper function is called
    """

    #Loop through each command and its variables
    for k, v in parsed_commands:

        #get function that matches the command
        fn = get_function(k)
        #pass variables into the command function
        fn(v) 


"""
input: a string (command)
output: a function that matches the command
"""

def get_function(command: str):
    
    if command == "make":
        return make_block() 

    """
    elif command == "x"
        return function_that_does_x
    """

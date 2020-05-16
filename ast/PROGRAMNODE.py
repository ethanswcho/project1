from libs.Node import Node

class Program(Node):

    def __init__(self):
        pass

    """
    input: list of string (tokens from text input)
    output: dictionary of "command_name": list_of_string
    """

    def parse(tokenized_input: list):

        parsed_commands = {}

        """
        Take in list of tokenized tokens from user_input, and parse through it.
        After parsing, tokens should be grouped per command (action) so next step (generate_game) can take the commands and translate it to python code.
        """

        """
        sample input:
        [  
            "make", "blue", "block", "block1", "at", "20", "40", "with", "40", "width", 
            "do", "every", "10", "second", "block1", "shift", "right", "by", "5", 
            "do", "every", "10", "second", "gravity", "increases", "by", "2"
        ]
        sample output:
        {
            "make": ["blue", "block", "block1", "at", "20", "40", "with", "40"],
            "do": ["every", "10", "second", "block1", "shift", "right", "by", "5"],
            "do": ["every", "10", "second", "gravity", "increases", "by", "2"]
        }
        """

        #stub
        return parsed_commands
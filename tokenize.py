"""
input: string loaded from input text file
output: list of tokens
"""

def tokenize(input_text: str):

    tokenized_input = []
    
    """
    parse through the input string and tokenize it into literals and user-inputs
    """

    """
    possible error handling:
        -Incorrect syntax/grammar
        -Invalid word
    error handling (TBD, only a suggestion):
        -after encountering the first case of error, return None and break()
    """

    """
    sample input:
    "
        make blue block block1 at 20, 40 with 40 width
        do every 10 second: block1 shift right by 5
        do every 10 second: gravity increases by 2
    "
    sample output:
    [
        "make", "blue", "block", "block1", "at", "20", "40", "with", "40", 
        "width", "do", "every", "10", "second", "block1", "shift", "right", "by", "5", 
        "do", "every", "10", "second", "gravity", "increases", "by", "2"
    ]
    """

    #stub
    return tokenized_input
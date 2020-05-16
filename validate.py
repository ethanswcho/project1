"""
input: dictionary of parsed commands
output: boolean (represents whether commands are valid), optinal notes (error messages)
"""

def validate(parsed_commands: dict):

    is_valid = True
    error_notes = []
    
    """
    run through parsed commands, and see if there are any typos or grammatically incorrect commands
    If there are issues, an error message (String) should be generated and added to error_notes
    """

    """
    sample implementation (with psuedo-code)
    
    for k, v in is_valid:
        if k or v is not valid:
            is_valid = False
            error_notes.append("error note generated using what part of this command is wrong")
    """

    #stub
    return is_valid, error_notes

"""
Generate the main method, integrate user inputted and translated methods, and return it.
"""


def build_main(code: list):

    main_start = "def main():\n"

    main_end = """    window.set()
        arcade.run()

    if __name __ == "__main__":
        main()
    """
    
    middle_code = """"""
    for line in code:
        middle_code = middle_code + "    " + line + "\n"
    
    return main_start + middle_code + main_end
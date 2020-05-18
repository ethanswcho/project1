class Tokenizer:

    program = None
    literals = None
    the_tokenizer = None

    def __init__(self, filename: str, literals_list: list):
        Tokenizer.literals = literals_list
        self.tokens = None
        self.current_token = 0
        try:
            with open(filename) as f:
                Tokenizer.program = f.read()
        except OSError:
            print("Didn't find file")
            exit()
        self.__tokenize()

    """
    Parses through the input string and tokenizes it into literals and user-inputs
    """
    def __tokenize(self):
        rw = "~"
        tokenized_program = self.program.replace("\n", "")
        print(tokenized_program)
        for s in self.literals:
            tokenized_program = tokenized_program.replace(s, rw + s + rw)
            print(tokenized_program)
        tokenized_program = tokenized_program.replace(rw + rw, rw)
        print(tokenized_program)
        if len(tokenized_program) > 0 and tokenized_program[0] == rw:
            tokenized_program = tokenized_program[1:]
        if len(tokenized_program) > 0 and tokenized_program[-1] == rw:
            tokenized_program = tokenized_program[:-1]
        self.tokens = tokenized_program.split(rw)
        print(self.tokens)
        for i in range(len(self.tokens)):
            self.tokens[i] = self.tokens[i].strip()
        print(self.tokens)

    """
    """
    def __check_next(self):
        token = ""
        if self.current_token < len(self.tokens):
            token = self.tokens[self.current_token]
        else:
            token = "NO_MORE_TOKENS"
        return token

    """
    """
    def get_next(self):
        token = ""
        if self.current_token < len(self.tokens):
            token = self.tokens[self.current_token]
            self.current_token += 1
        else:
            token = "NULLTOKEN"
        return token

    """
    """
    def check_token(self, regexp: str):
        s = self.__check_next()
        print("comparing: |" + s + "|  to  |" + regexp + "|")
        return s.matches(regexp)

    """
    """
    def get_and_check_next(self, regexp: str):
        s = self.get_next()
        if not s.matches(regexp):
            raise Exception("Unexpected next token for Parsing! Expected something matching: " + regexp + " but got: " + s)
        print("matched: " + s + "  to  " + regexp)
        return s

    """
    Create singleton
    """
    @staticmethod
    def make_tokenizer(filename: str, literals: list):
        if Tokenizer.the_tokenizer is None:
            Tokenizer.the_tokenizer = Tokenizer(filename, literals)

    """
    Get singleton instance
    """
    @staticmethod
    def get_tokenizer():
        return Tokenizer.the_tokenizer

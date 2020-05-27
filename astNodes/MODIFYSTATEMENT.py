from astNodes.CHANGESTATEMENT import CHANGESTATEMENT
from astNodes.MOVESTATEMENT import MOVESTATEMENT
from astNodes.REMOVESTATEMENT import REMOVESTATEMENT
from astNodes.SETSTATEMENT import SETSTATEMENT
from libs.node import Node

# Constants
DESTROY = "destroy"
SET = "set"
CHANGE = "change"
MOVE = "move"


class MODIFYSTATEMENT(Node):

    def __init__(self):
        self.statement = None
        super().__init__()

    def parse(self):
        if self.tokenizer.check_token(DESTROY):
            s = REMOVESTATEMENT()
        elif self.tokenizer.check_token(SET):
            s = SETSTATEMENT()
        elif self.tokenizer.check_token(CHANGE):
            s = CHANGESTATEMENT()
        elif self.tokenizer.check_token(MOVE):
            s = MOVESTATEMENT()
        else:
            raise Exception("Unexpected next token for Parsing! Expected something matching: destroy|set|change|move")

        s.parse()
        self.statement = s

    def evaluate(self, args):
        return self.statement.evaluate(args)

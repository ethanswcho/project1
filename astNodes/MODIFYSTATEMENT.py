from astNodes.CHANGESTATEMENT import CHANGESTATEMENT
from astNodes.MOVESTATEMENT import MOVESTATEMENT
from astNodes.REMOVESTATEMENT import REMOVESTATEMENT
from astNodes.SETSTATEMENT import SETSTATEMENT
from libs.Node import Node

# Constants
REMOVE = "remove"
SET = "set"
CHANGE = "change"
MOVE = "move"


class MODIFYSTATEMENT(Node):

    def __init__(self):
        self.statement = None
        self.type = None
        super().__init__()

    def parse(self):
        if self.tokenizer.check_token("destroy"):
            s = REMOVESTATEMENT()
            self.type = REMOVE
        elif self.tokenizer.check_token("set"):
            s = SETSTATEMENT()
            self.type = SET
        elif self.tokenizer.check_token("change"):
            s = CHANGESTATEMENT()
            self.type = CHANGE
        elif self.tokenizer.check_token("move"):
            s = MOVESTATEMENT()
            self.type = MOVE
        else:
            raise Exception("Unexpected next token for Parsing! Expected something matching: destroy|set|change|move")

        s.parse()
        self.statement = s

    def evaluate(self):
        self.statement.evaluate()

    def get_fields(self):
        return{
            "statement": self.statement.get_fields(),
            "type": self.type
        }

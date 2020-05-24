from astNodes.MAKESTATEMENT import MAKESTATEMENT
from astNodes.MODIFYSTATEMENT import MODIFYSTATEMENT
from libs.node import Node

# Constants
MAKE = "make"


class STATEMENT(Node):

    def __init__(self):
        self.statement = None
        self.type = None
        super().__init__()

    def parse(self):
        if self.tokenizer.check_token("make a"):
            s = MAKESTATEMENT()
            s.parse()
            self.statement = s
            self.type = MAKE
        else:
            s = MODIFYSTATEMENT()
            s.parse()
            self.statement = s.statement
            self.type = s.type

    def evaluate(self, args):
        return self.statement.evaluate(args)

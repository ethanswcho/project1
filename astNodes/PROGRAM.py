from astNodes.ARENA import ARENA
from astNodes.LOOPSTATEMENT import LOOPSTATEMENT
from astNodes.MAKESTATEMENT import MAKESTATEMENT
from astNodes.MODIFYSTATEMENT import MODIFYSTATEMENT
from libs.Node import Node


class PROGRAM(Node):

    def __init__(self):
        self.arena = ARENA()
        self.make_statements = []
        self.modify_statements = []
        self.loops = []
        super().__init__()

    def parse(self):
        if self.tokenizer.check_token("arena size"):
            self.arena.parse()

        while self.tokenizer.more_tokens():
            if self.tokenizer.check_token("make a"):
                s = MAKESTATEMENT()
                s.parse()
                self.make_statements.append(s)
            elif self.tokenizer.check_token("do every"):
                s = LOOPSTATEMENT()
                s.parse()
                self.loops.append(s)
            else:
                s = MODIFYSTATEMENT()
                s.parse()
                self.modify_statements.append(s)

    def evaluate(self):
        # TODO
        pass

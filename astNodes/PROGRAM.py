from astNodes.ARENA import ARENA
from astNodes.LOOPSTATEMENT import LOOPSTATEMENT
from astNodes.MAKESTATEMENT import MAKESTATEMENT
from astNodes.MODIFYSTATEMENT import MODIFYSTATEMENT
from astNodes.PLAYER import PLAYER
from libs.node import Node


class PROGRAM(Node):

    def __init__(self):
        self.arena = ARENA()
        self.player = PLAYER()
        self.make_statements = []
        self.modify_statements = []
        self.loops = []
        super().__init__()

    def parse(self):
        if self.tokenizer.check_token("arena size"):
            self.arena.parse()

        if self.tokenizer.check_token("put player"):
            self.player.parse()

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
        pass

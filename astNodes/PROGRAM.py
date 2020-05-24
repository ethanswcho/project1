from astNodes.ARENA import ARENA
from astNodes.LOOPSTATEMENT import LOOPSTATEMENT
from astNodes.MAKESTATEMENT import MAKESTATEMENT
from astNodes.MODIFYSTATEMENT import MODIFYSTATEMENT
from libs.node import Node


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

        # check for player positions
        xpos_set = False
        ypos_set = False
        i = 0
        while i < 2:
            if self.tokenizer.check_token("set") and self.tokenizer.tokens[self.tokenizer.current_token + 3] == "player":
                if self.tokenizer.tokens[self.tokenizer.current_token + 1] == "xpos":
                    xpos_set = True
                elif self.tokenizer.tokens[self.tokenizer.current_token + 1] == "ypos":
                    ypos_set = True
                s = MODIFYSTATEMENT()
                s.parse()
                self.modify_statements.append(s)
            else:
                raise Exception("Please set the default player position in your config file.")
            i += 1

        if not ypos_set and xpos_set:
            raise Exception("Please set the default player position in your config file.")

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

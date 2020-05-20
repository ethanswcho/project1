from libs.Node import Node
import re


class FIELD(Node):

    def __init__(self):
        self.field = None
        self.type = None
        super().__init__()

    def parse(self):
        self.field = self.tokenizer.get_and_check_next("xpos|ypos|width|height|colour")
        if self.field == "colour":
            self.type = "colour"
        elif re.match("xpos|ypos|width|height", self.field):
            self.type = "number"
        else:
            self.type = "string"

    def evaluate(self):
        # TODO
        pass

from libs.node import Node


class FIELD(Node):

    def __init__(self):
        self.field = None
        super().__init__()

    def parse(self):
        self.field = self.tokenizer.get_and_check_next("xpos|ypos")

    def evaluate(self):
        pass

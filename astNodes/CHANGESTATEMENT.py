from astNodes.FIELD import FIELD
from libs.Node import Node


class CHANGESTATEMENT(Node):

    def __init__(self):
        self.object = None
        self.field = None
        self.value = None
        super().__init__()

    def parse(self):
        self.tokenizer.get_and_check_next("change")
        field = FIELD()
        field.parse()
        if field.type == "string":
            raise Exception("Expected a number field, got a string field")
        self.field = field

        self.tokenizer.get_and_check_next("of")
        self.object = self.tokenizer.get_next()

        self.tokenizer.get_and_check_next("by")
        self.value = int(self.tokenizer.get_next())

    def evaluate(self):
        # TODO
        pass

from astNodes.FIELD import FIELD
from libs.node import Node

#CHANGESTATEMENT ::= "change" NUMBERFIELD "of" OBJECT "by" DIGIT

class CHANGESTATEMENT(Node):

    def __init__(self):
        self.block_name = None
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
        self.block_name = self.tokenizer.get_next()

        self.tokenizer.get_and_check_next("by")
        self.value = int(self.tokenizer.get_next())

    def evaluate(self, wait):
        return "".join((f"        pyglet.clock.schedule_once(",
                        f"self.{self.block_name}.change_block_{self.field.field}, ",
                        f"{wait}, {self.value})"))

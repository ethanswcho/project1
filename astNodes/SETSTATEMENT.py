from astNodes.FIELD import FIELD
from libs.node import Node


class SETSTATEMENT(Node):

    def __init__(self):
        self.block_name = None
        self.field = None
        self.value = None
        super().__init__()

    def parse(self):
        self.tokenizer.get_and_check_next("set")
        field = FIELD()
        field.parse()
        self.field = field

        self.tokenizer.get_and_check_next("of")
        self.block_name = self.tokenizer.get_next()

        self.tokenizer.get_and_check_next("to")
        self.value = int(self.tokenizer.get_next())

    def evaluate(self, wait=0):
        return "".join((f"        pyglet.clock.schedule_once(",
                        f"lambda dt: self.{self.block_name}.set_block_{self.field.field}("
                        f"dt, {self.value}), {wait})"))

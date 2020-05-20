from libs.Node import Node


class MOVESTATEMENT(Node):

    def __init__(self):
        self.block_name = None
        self.direction = None
        self.value = None
        super().__init__()

    def parse(self):
        self.tokenizer.get_and_check_next("move")
        self.block_name = self.tokenizer.get_next()
        self.direction = self.tokenizer.get_and_check_next("up|down|left|right")
        self.tokenizer.get_and_check_next("by")
        self.value = int(self.tokenizer.get_next())

    def evaluate(self):
        # TODO
        pass

    def get_fields(self):
        return{
            "block_name": self.block_name,
            "direction": self.direction,
            "value": self.value
        }
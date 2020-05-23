from libs.node import Node


class REMOVESTATEMENT(Node):

    def __init__(self):
        self.block_name = None
        super().__init__()

    def parse(self):
        self.tokenizer.get_and_check_next("destroy")
        self.block_name = self.tokenizer.get_next()

    def evaluate(self, wait=None):
        pass

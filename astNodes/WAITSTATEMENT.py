from libs.Node import Node


class WAITSTATEMENT(Node):

    def __init__(self):
        self.ms = None
        super().__init__()

    def parse(self):
        self.tokenizer.get_and_check_next("wait")
        self.ms = int(self.tokenizer.get_next())
        self.tokenizer.get_and_check_next("ms")

    def evaluate(self):
        # TODO
        pass
    
    def get_fields(self):
        return{
            "ms": self.ms
        }
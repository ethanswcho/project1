from libs.node import Node


class COLOUR(Node):

    def __init__(self):
        self.colour = None
        super().__init__()

    def parse(self):
        #self.colour = self.tokenizer.get_and_check_next("#(\d|[A-Fa-f])+")
        self.colour = self.tokenizer.get_and_check_next("\\.*")

    def evaluate(self):
        # TODO
        pass

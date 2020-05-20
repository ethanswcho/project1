from astNodes.COLOUR import COLOUR
from astNodes.FIELD import FIELD
from libs.Node import Node


class SETSTATEMENT(Node):

    def __init__(self):
        self.object = None
        self.field = None
        self.value = None
        super().__init__()

    def parse(self):
        self.tokenizer.get_and_check_next("set")
        field = FIELD()
        field.parse()
        self.field = field

        self.tokenizer.get_and_check_next("of")
        self.object = self.tokenizer.get_next()

        self.tokenizer.get_and_check_next("to")
        if field.type == "number":
            self.value = int(self.tokenizer.get_next())
        elif field.type == "colour":
            colour = COLOUR()
            colour.parse()
            self.value = colour.colour
        else:
            self.value = self.tokenizer.get_next()

    def evaluate(self):
        # TODO
        pass

    def get_fields(self):
        output = {
            "object": self.object
        }
        fields = self.field.get_fields()
        for k, v in fields.items():
            output[k] = v
        output["value"] = self.value
        return output
            

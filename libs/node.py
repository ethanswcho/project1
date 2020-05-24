from abc import ABC, abstractmethod
from libs.tokenizer import Tokenizer


class Node(ABC):

    def __init__(self):
        self.tokenizer = Tokenizer.get_tokenizer()

    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def evaluate(self, *args):
        pass

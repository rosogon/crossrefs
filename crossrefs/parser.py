__author__ = 'roman'


from tokenizer import Tokenizer
from tokenizer import Token
from tokenizer import Kinds


class Node(object):
    pass


class ItemName(Node):
    pass


class ItemContent(Node):
    pass


class Paragraph(Node):
    pass


class Chunk(Node):
    pass


class CrossReference(Node):
    pass


class Parser(object):

    def __init__(self, tokenizer_):
        self.tokenizer = tokenizer_

    def _parse1(self):
        items = set()
        for token in self.tokenizer.nexttoken():
            if token.is_(Kinds.ITEM):
                items.add(token.value)
        return items

    def _parse1a(self):

        from itertools import ifilter
        items = set(
            map(
                lambda x: x.value,
                ifilter(
                    lambda x: x.is_(Kinds.ITEM),
                    self.tokenizer.nexttoken()
                )
            )
        )
        return items

    def _parse1b(self):
        items = [
            token.value
            for token in self.tokenizer.nexttoken()
            if token.is_(Kinds.ITEM)
        ]
        return items

    def parse(self, file_):
        self.tokenizer.init(file_)
        items = self._parse1()
        print (items)


if __name__ == "__main__":
    with open("../mitologia.pre") as f:
        tokenizer = Tokenizer()
        parser = Parser(tokenizer)
        parser.parse(f)

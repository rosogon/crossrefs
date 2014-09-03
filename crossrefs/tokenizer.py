__author__ = 'roman'


class Kinds(object):
    ITEM = 0
    WORD = 1


class Token(object):

    def __init__(self, kind, value):
        self._kind = kind
        self._value = value

    def is_(self, kind):
        return kind == self._kind

    @property
    def kind(self):
        return self._kind

    @property
    def value(self):
        return self._value

    def __repr__(self):
        return "<Token(kind={}, value={})>".format(
            repr(self._kind), repr(self._value))

    def __str__(self):
        #return str((self._kind, self._value))
        return self._value

    def __eq__(self, other):
        if other is None:
            return False
        return (self._kind == other.kind) and (self._value == other.value)

class Tokenizer(object):

    class ParseError(Exception):
        def __init__(self, msg):
            self.message = msg

    def __init__(self):
        """
        """
        self.init()
        #self.f = None
        #self.nline = 0
        #self.words = []
        #self.index = 0

    def init(self, file_=None):
        self.f = file_
        self.nline = 0
        self.words = []
        self.index = 0

        if file_ is not None:
            self.f.seek(0)

    def readline(self):
        """Generator returning a line on each call.

        Line ends with CR if file line ends in CR.

        :rtype : str
        """
        for line in self.f:
            self.nline += 1
            yield line

        return

    def nextword(self):
        """Reads next word from line.

        Always (even on EOF w/o CR) returns CR on EOL

        :rtype : str
        """
        for line in self.readline():
            words = line.split()
            words.append("\n")
            for word in words:
                yield word

        return

    def nexttoken(self):
        item = ""
        in_item = False
        sep = ""
        for word in self.nextword():
            if not in_item and word[0] == "[":
                item = ""
                in_item = True
                sep = ""
            if in_item:
                item += sep + word
                sep = " "
                if word[-1] == "]":
                    in_item = False
                    yield Token(Kinds.ITEM, item[1:-1])
                continue
            else:
                yield Token(Kinds.WORD, word)

        return


if __name__ == "__main__":
    with open("/tmp/lineas.txt") as f:
        t = Tokenizer()
        t.init(f)
        for w in t.nexttoken():
            print repr(w), w
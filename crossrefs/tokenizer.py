# -*- coding: utf-8 -*-
import unicodedata


class Kinds(object):
    PUNCTUATION = 0
    WORD = 1
    ITEM = 2
    CROSSREF = 3


def normalize(s):
    if type(s) is str:
        s1 = s
    else:
        s1 = unicodedata.normalize('NFKD', s).encode('ASCII', 'ignore')
    s2 = s1.upper()
    return s2


class Token(object):

    def __init__(self, kind, value):
        self._kind = kind
        self._value = value
        self._normvalue = normalize(value) if kind != Kinds.PUNCTUATION \
            else value

    def crossref(self):
        t = Token(0, "")
        t._kind = Kinds.CROSSREF
        t._value = self._value
        t._normvalue = self._normvalue
        return t

    def is_(self, kind):
        return kind == self._kind

    @property
    def kind(self):
        return self._kind

    @property
    def value(self):
        return self._value

    @property
    def normvalue(self):
        return self._normvalue

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

    def init(self, file_=None):
        self._f = file_
        self._nline = 0

        if file_ is not None:
            self._f.seek(0)

    def lines(self):
        """Generator returning a line on each call.

        Line ends with CR if file line ends in CR.

        :rtype : str
        """
        for line in self._f:
            self._nline += 1
            if line[-1] != "\n":
                line = line + "\n"
            yield line

        return

    def words(self):
        """Reads next word from line.

        Always (even on EOF w/o CR) returns CR on EOL

        :rtype : str
        """
        for line in self.lines():
            words = line.split()
            words.append("\n")
            for word in words:
                yield word

        return

    def tokens(self):
        item = ""
        word = ""
        in_item = False
        in_word = False
        for line in self.lines():
            for ch in line:
                if not in_item and ch == "[":
                    item = ""
                    in_item = True

                if in_item:
                    item += ch
                    if ch == "]":
                        in_item = False
                        yield Token(Kinds.ITEM, item[1:-1])

                elif in_word:
                    if ch.isalpha() or ch.isdigit():
                        word = word + ch
                    else:
                        in_word = False
                        yield Token(Kinds.WORD, word)
                        yield Token(Kinds.PUNCTUATION, ch)

                elif ch.isalpha():
                    in_word = True
                    word = ch
                else:
                    yield Token(Kinds.PUNCTUATION, ch)
        return

    def tokens_(self):
        item = ""
        in_item = False
        sep = ""
        for word in self.words():
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

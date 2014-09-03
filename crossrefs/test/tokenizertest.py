__author__ = 'roman'

import unittest
from StringIO import StringIO

from crossrefs.tokenizer import Tokenizer
from crossrefs.tokenizer import Token
from crossrefs.tokenizer import Kinds


class TokenizerTestCase(unittest.TestCase):

    def test_readline(self):
        t = Tokenizer()
        l1 = "linea1\n"
        l2 = "linea2\n"
        l3 = "linea3"

        s = "{}{}{}".format(l1, l2, l3)
        f = StringIO(s)
        t.init(f)

        g = t.readline()
        self.assertEquals(l1, g.next())
        self.assertEquals(l2, g.next())
        self.assertEquals(l3, g.next())

    def test_nextword(self):
        t = Tokenizer()
        s = "word1 word2\n  word3\n\tword4   "
        t.init(StringIO(s))

        words = ["word1", "word2", "\n", "word3", "\n", "word4", "\n"]
        g = t.nextword()
        for word in words:
            self.assertEquals(word, g.next())

        try:
            g.next()
        except StopIteration:
            pass

    def test_nexttoken(self):
        t = Tokenizer()
        s = "[item1] word1 [item2] word2"
        t.init(StringIO(s))

        tokens = [
            Token(Kinds.ITEM, "item1"),
            Token(Kinds.WORD, "word1"),
            Token(Kinds.ITEM, "item2"),
            Token(Kinds.WORD, "word2")
        ]

        g = t.nexttoken()
        for token in tokens:
            self.assertEquals(token, g.next())

        try:
            g.next()
        except StopIteration:
            pass

    def test_something(self):
        #self.assertEqual(True, False)
        pass


if __name__ == '__main__':
    unittest.main()

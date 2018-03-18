# -*- coding: utf-8 -*-

import unittest
from StringIO import StringIO

from crossrefs.tokenizer import Tokenizer
from crossrefs.tokenizer import Token
from crossrefs.tokenizer import Kinds
from crossrefs.tokenizer import normalize as n


class TokenizerTestCase(unittest.TestCase):

    def test_readline(self):
        t = Tokenizer()
        l1 = "linea1\n"
        l2 = "linea2\n"
        l3 = "linea3"

        s = "{}{}{}".format(l1, l2, l3)
        f = StringIO(s)
        t.init(f)

        g = t.lines()
        self.assertEquals(l1, g.next())
        self.assertEquals(l2, g.next())
        self.assertEquals(l3 + "\n", g.next())

    def test_nexttoken(self):
        t = Tokenizer()
        s = u"[item1] word1 [item2] word2(ícaro)"
        t.init(StringIO(s))

        tokens = [
            Token(Kinds.ITEM, u"item1"),
            Token(Kinds.PUNCTUATION, u" "),
            Token(Kinds.WORD, u"word1"),
            Token(Kinds.PUNCTUATION, u" "),
            Token(Kinds.ITEM, u"item2"),
            Token(Kinds.PUNCTUATION, u" "),
            Token(Kinds.WORD, u"word2"),
            Token(Kinds.PUNCTUATION, u"("),
            Token(Kinds.WORD, u"ícaro"),
            Token(Kinds.PUNCTUATION, u")")
        ]

        g = t.tokens()
        for expected in tokens:
            actual = g.next()
            self.assertEquals(expected, actual)

        try:
            g.next()
        except StopIteration:
            pass

    def test_normalize(self):
        self.assertEquals(n(u"word"), "WORD")
        self.assertEquals(n(u"á"), "A")
        self.assertEquals(n(u"ícarO"), "ICARO")
        self.assertEquals(n(u"a."), "A.")

if __name__ == '__main__':
    unittest.main()

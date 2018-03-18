# -*- coding: utf-8 -*-
from __future__ import print_function

import io
import sys

from tokenizer import Tokenizer
from tokenizer import Kinds
from tokenizer import Token

import output


class Parser(object):

    def __init__(self, tokenizer_, outputer_):
        self.tokenizer = tokenizer_
        self.outputer = outputer_

    def _parse1(self):
        items = {
            t.normvalue: t
            for t in self.tokenizer.tokens()
            if t.is_(Kinds.ITEM)
        }
        return items

    def _parse2(self, items):
        self.outputer.begin()
        for t in self.tokenizer.tokens():
            if t.is_(Kinds.WORD) and t.normvalue in items:
                t = t.crossref()

            self.outputer.out(t)
        self.outputer.end()

    def parse(self, file_):
        self.tokenizer.init(file_)
        items = self._parse1()
        self.tokenizer.init(file_)
        #with io.open(sys.stdout, encoding="utf-8") as out:
        self._parse2(items)


if __name__ == "__main__":
    with io.open("old/mitologia.pre", encoding="utf-8") as f:
        tokenizer = Tokenizer()
        outputer = output.HtmlOutputer()
        parser = Parser(tokenizer, outputer)
        parser.parse(f)

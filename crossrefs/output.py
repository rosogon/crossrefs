# -*- coding: utf-8 -*-
from __future__ import print_function

from tokenizer import Kinds


def p(s, *args, **kwargs):
    print(s.encode("utf-8"), *args, **kwargs)


class HtmlOutputer(object):

    def __init__(self):
        self.newpara = False
        self.closepara = False

    def begin(self):
        p('<html>')
        p('<head><meta charset="UTF-8"></head>')
        p('<body>')

    def out(self, t):
        if self.newpara:
            p('<p>', end="")
            self.newpara = False
            self.closepara = True

        if t.is_(Kinds.ITEM):
            if self.closepara:
                p("</p>")
                self.closepara = False
            p(u'<h2><a name="{}">{}</a></h2>'.format(t.normvalue, t.value))
            self.newpara = True
        elif t.is_(Kinds.CROSSREF):
            p(u'<a href="#{}">{}</a>'.format(t.normvalue, t.value), end="")
        else:
            p(u'{}'.format(t.value), end="")

    def end(self):
        if self.closepara:
            p("</p>")
        p("</body>")
        p("</html>")


class MarkDownOutputer(object):

    def __init__(self):
        pass

    def begin(self):
        pass

    def out(self, t):
        if t.is_(Kinds.ITEM):
            p(u'## <a name="{}">{}</a> ##'.format(t.normvalue, t.value))
        elif t.is_(Kinds.CROSSREF):
            p(u'<a href="#{}">{}</a>'.format(t.normvalue, t.value), end="")
        else:
            p(u'{}'.format(t.value), end="")

    def end(self):
        pass

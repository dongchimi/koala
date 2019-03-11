import unittest

import sys

from koala import ExcelCompiler


class TestUserExcel(unittest.TestCase):

    def setUp(self):
        c = ExcelCompiler("../files/source.xlsx")
        self.graph = c.gen_graph()
        sys.setrecursionlimit(10000)

    def test_content(self):
        print("Loading from compiled file...")
        print("D1 is %s" % self.graph.evaluate('LF몰_PC브랜드검색!C4'))
        print('evaluate start...2')
        print("D1 is %s" % self.graph.evaluate('LF몰_PC브랜드검색!I48'))

        print('evaluate end...')


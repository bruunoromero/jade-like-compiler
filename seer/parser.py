from .tree import *


class _Walker(object):

    def __init__(self, file_name):
        self.__file_name = file_name
        self.__row = 0
        self.__col = 0
        self.__lines = []
        self.__to_lines()
        self.__curr_line = self.__lines[self.__row]

    def __to_lines(self):
        lines = open(self.__file_name, 'r')
        for line in lines:
            self.__lines.append(line)
        lines.close()

    def __next_line(self):
        self.__row += 1
        self.__col = 0
        self.__curr_line = self.__lines[self.__row]

    def has_next(self):
        try:
            if self.__col is len(self.__lines[self.__row]):
                self.__next_line()
            return self.__lines[self.__row][self.__col]
        except:
            return False

    def next(self):
        try:
            res = self.__lines[self.__row][self.__col]
            self.__col += 1
            return res
        except:
            return None

    def peek(self):
        try:
            return self.__lines[self.__row][self.__col]
        except:
            return None


class Parser(object):

    def __init__(self, file_name):
        self.__file_name = file_name
        self.__self_nodes = []
        self.__set_self_nodes()
        self.__walker = _Walker(file_name)
        self.__prog = Program()
        self.__stack = []

    def __set_self_nodes(self):
        self.__self_nodes = [
            'area',
            'base',
            'br',
            'col',
            'command',
            'embed',
            'hr',
            'img',
            'input',
            'keygen',
            'link',
            'meta',
            'param',
            'source',
            'track',
            'wbr'
        ]

    def __read_tag(self, char, level):
        acc = char
        attr = []

        while self.__walker.has_next():
            tok = self.__walker.next()

            if tok is '\n':
                pass



    def parse(self):
        level = ""

        while self.__walker.has_next():
            tok = self.__walker.next()

            if tok.isalpha():
                self.__read_tag(tok, level)

            elif tok is '\n':
                level = ""

            elif tok.isspace():
                level += 1

            else:
                print('sei la')






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
        pass


class Parser(object):

    def __init__(self, file_name):
        self.__file_name = file_name
        self.__default_nodes = []
        self.__set_default_nodes()
        self.__walker = _Walker(file_name)


    def __set_default_nodes(self):
        self.__default_nodes = [
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

    def parse(self):
        while self.__walker.has_next():
            print(self.__walker.next())




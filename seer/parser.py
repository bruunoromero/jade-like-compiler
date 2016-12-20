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
        self.__lines.append('\n')
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
        self.__stack = [self.__prog]

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

    def __skip_line(self):
        acc = ""

        while self.__walker.has_next():
            tok = self.__walker.next()

            if tok is '\n':
                return

            if tok.isspace():
                acc += tok
                continue

            raise Exception('Unexpected text {}. Self closing tags should not have any child'.format(acc))

    def __read_text(self, char=""):
        acc = char

        while self.__walker.has_next():
            tok = self.__walker.next()

            if tok is '\n':
                return acc
            else:
                acc += tok

        return acc

    def __read_attrs(self):
        attrs = []
        attr = {}
        name = ''
        value = ''
        found_equals = False

        while self.__walker.has_next():
            tok = self.__walker.next()

            if tok is ')':
                return attrs

            if (tok.isspace() and (not self.__walker.peek().isspace())) or tok is ',' or self.__walker.peek() is ')':
                if self.__walker.peek() is ')':
                    if found_equals:
                        value += tok
                    else:
                        name += tok

                if not value:
                    if not name:
                        continue
                    value = name

                if value.count('"') > 0 or value.count("'") > 0:
                    raise Exception("Attributes could not contain quotes")

                attr['name'] = name
                attr['value'] = value
                name = ''
                value = ''
                attrs.append(attr)
                attr = {}
                found_equals = False
                continue

            if tok is '=':
                found_equals = True
                continue

            if not found_equals:
                name += tok
            else:
                value += tok

        raise Exception('Could not parse this shitty code')

    def __find_parent(self, level):
        while len(self.__stack) > 0:
            if self.__stack[-1].indent < level:
                return self.__stack[-1]
            else:
                self.__stack.pop()

        raise Exception("Could not parse this shitty code")

    def __add_node(self, level, acc, attr, last, text=""):
        parent = self.__find_parent(level)
        if acc not in self.__self_nodes:
            if text:
                text_node = TextNode(text)
                node = DefaultNode(acc, level, attr, [text_node])
            else:
                node = DefaultNode(acc, level, attr, [])
            parent.append_child(node)
            self.__stack.append(node)
        else:
            if text:
                raise Exception('Unexpected text {}. Self closing tags should not have any child'.format(text))
            elif last is not '\n':
                self.__skip_line()
            node = SelfNode(acc, level, attr)
            parent.append_child(node)
            self.__stack.append(node)

    def __read_tag(self, char, level):
        acc = char
        attr = []

        while self.__walker.has_next():
            tok = self.__walker.next()
            if tok.isalpha() or tok.isdigit() or tok is '-':
                acc += tok
                continue

            if tok is '\n':
                self.__add_node(level, acc, attr, tok)
                break

            if tok is '(':
                attr = self.__read_attrs()
                continue

            if tok.isspace():
                text = self.__read_text()
                self.__add_node(level, acc, attr, tok, text)
                break

            raise Exception('could not parse identifier {}'.format(tok))

    def parse(self):
        level = 0

        while self.__walker.has_next():
            tok = self.__walker.next()

            if tok.isalpha() or tok.isdigit():
                self.__read_tag(tok, level)
                level = 0
                continue

            if tok is '\n':
                level = 0
                continue

            if tok.isspace():
                level += 1
                continue

            text = self.__read_text(' ' * level + tok)
            text_node = TextNode(text)
            parent = self.__find_parent(level)
            parent.append_child(text_node)
            level = 0

        return self.__prog






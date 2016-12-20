class Node(object):

    def __init__(self, indent):
        self.__indent = indent

    @property
    def indent(self):
        return self.__indent


class Program(Node):

    def __init__(self, children=[]):
        super(Program, self).__init__(-1)
        self.__children = children

    @property
    def children(self):
        return self.__children

    def append_child(self, child):
        self.__children.append(child)


class TextNode(object):

    def __init__(self, text=""):
        super(TextNode, self).__init__()
        self.__text = text

    @property
    def text(self):
        return self.__text

    def append_text(self, t):
        self.__text += t


class SelfNode(Node):

    def __init__(self, name, indent, attributes=[]):
        super(SelfNode, self).__init__(indent)
        self.__name = name
        self.__attributes = attributes
        self.__indent = indent

    @property
    def name(self):
        return self.__name

    @property
    def indent(self):
        return self.__indent

    @property
    def attributes(self):
        return self.__attributes

    def append_attr(self, attr):
        self.__attributes.append(attr)


class DefaultNode(SelfNode):

    def __init__(self, name, indent, attributes=[], children=[]):
        super(DefaultNode, self).__init__(name, indent, attributes)
        self.__children = children

    @property
    def children(self):
        return self.__children

    def append_child(self, child):
        self.__children.append(child)




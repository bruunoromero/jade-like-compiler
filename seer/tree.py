from abc import ABCMeta
from functools import reduce



class INode(metaclass=ABCMeta):
    pass


class Program(object):

    def __init__(self, children=[]):
        self.__children = children

    @property
    def children(self):
        return self.__children

    def append_child(self, child):
        self.__children.append(child)


class Node(INode):

    def __init__(self, parent):
        self.__parent = parent

    @property
    def parent(self):
        return self.__parent


class TextNode(Node):

    def __init__(self, parent, text=""):
        super(TextNode, self).__init__(parent)
        self.__text = text

    @property
    def text(self):
        return self.__text

    def append_text(self, t):
        self.__text += t


class SelfNode(Node):

    def __init__(self, parent, indent=0, attributes=[]):
        super(SelfNode, self).__init__(parent)
        self.__attributes = attributes
        self.__indent = indent

    @property
    def indent(self):
        return self.__indent

    @property
    def attributes(self):
        return self.__attributes

    def append_attr(self, attr):
        self.__attributes.append(attr)


class DefaultNode(SelfNode):

    def __init__(self, parent, indent=0, attributes=[], children=[]):
        super(DefaultNode, self).__init__(parent, indent, attributes)
        self.__children = children

    @property
    def children(self):
        return self.__children

    def append_child(self, child):
        self.__children.append(child)




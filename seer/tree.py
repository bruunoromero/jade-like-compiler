from abc import ABCMeta


class INode(metaclass=ABCMeta):
    pass


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

    def __init__(self, parent, attributes=[]):
        super(SelfNode, self).__init__(parent)
        self.__attributes = attributes

    @property
    def attributes(self):
        return self.__attributes

    def append_attr(self, attr):
        self.__attributes.append(attr)


class DefaultNode(SelfNode):

    def __init__(self, parent, attributes=[], children=[]):
        super(DefaultNode, self).__init__(parent, attributes)
        self.__children = children

    @property
    def children(self):
        return self.__children

    def append_child(self, child):
        self.__children.append(child)




from seer.tree import *


class Compiler(object):

    def __init__(self, tree):
        self.__tree = tree

    def traverse(self, node):
        if isinstance(node, DefaultNode):
            print(node.name + '   ' + str(node.children))
            for child in node.children:
                self.traverse(child)
        else:
            print(node.name)


    def __compile(self, node, level=0):
        if isinstance(node, TextNode):
            return ' ' * level + node.text

        if isinstance(node, DefaultNode):
            acc = ' ' * level + '<' + node.name
            for attr in node.attributes:
                acc += ' '+ attr['name'] + '=' + "\"" + attr['value'] + "\""
            acc += '>\n'
            for child in node.children:
                acc += self.__compile(child, level + 2) + '\n'
            acc += ' ' * level + '</' + node.name + '>'
            return acc

        if isinstance(node, SelfNode):
            acc = ' ' * level + '<' + node.name + ' '
            for attr in node.attributes:
                acc += attr['name'] + '=' + "\"" + attr['value'] + "\"" + " "
            acc += ' />'
            return acc

        raise Exception('Unexpected node dude, shitty code as fuck!')

    def compile(self):
        # for child in self.__tree.children:
        #     self.traverse(child)
        if isinstance(self.__tree, Program):
            acc = ""
            for child in self.__tree.children:
                acc += self.__compile(child)

            return acc

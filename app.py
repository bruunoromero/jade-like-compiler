from seer import Parser
from seer.compiler import Compiler

# p = Parser('C:\\Users\\951546190\\Desktop\\learn-python\\teste.pug')
# p = Parser('C:\\Users\\bruno.romero\\Desktop\\learn-python\\teste.pug')


p = Parser('/Users/bruno/Desktop/Python/teste.pug')
tree = p.parse()
c = Compiler(tree)
code = c.compile()
print(code)

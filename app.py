from seer import Parser
from seer.compiler import Compiler

p = Parser('/Users/bruno/Desktop/Python/teste.seer')
tree = p.parse()
c = Compiler(tree)
code = c.compile()
print(code)

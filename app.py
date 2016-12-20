from seer import Parser, Compiler

p = Parser('/Users/bruno/Desktop/Python/teste.seer')
tree = p.parse()
c = Compiler(tree)
code = c.compile()
print(code)

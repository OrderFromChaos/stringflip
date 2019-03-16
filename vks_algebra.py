import pyparsing as pp
from functools import reduce
import sys

def Syntax():
    lpar  = pp.Literal( '(' ).suppress()
    rpar  = pp.Literal( ')' ).suppress()
    substr = pp.Word(pp.alphanums)
    expr = pp.Forward()
    atom = substr | pp.Group(lpar + expr + rpar)
    expr << atom + pp.ZeroOrMore(atom)
    return expr

expr = Syntax()
res = expr.parseString(sys.argv[1])
print(res)

# Now act on this tokenized string:
# ['abc', [[['A'], ['B']], 'C']]

class Substr:
    def __init__(self, content, flipbit):
        self.content = content
        self.flipbit = flipbit
    def __repr__(self):
        if self.flipbit == 1:
            return str(self.content)
        else:
            return str(self.content[::-1])
    def __add__(self, other):
        return Substr(self.content[::self.flipbit] + other.content[::other.flipbit],1)

parseListType = type(res)

def recurseAlgebra(obj):
    if type(obj) == str:
        return Substr(obj, 1)
    else: # If not a string, it's a type parseListType or list
        intermediate = []
        for index, elm in enumerate(obj):
            if type(elm) == parseListType or type(elm) == list:
                # Apply recurseAlgebra to deal with sublist
                for newstr in recurseAlgebra(elm):
                    intermediate.append(newstr)
            else: # It's of type string
                intermediate.append(Substr(elm, 1))
        # Now the intermediate list should be a collection of strings
        return [Substr(x.content,x.flipbit*-1) for x in intermediate[::-1]]

output = recurseAlgebra([res])
print(reduce((lambda x, y: x + y),output))

def flipstring(s: str) -> str:
    # Tokenize string
    def recurseTokenize(startpos):
        output = []
        tempchars = []
        i = startpos
        while i < len(s):
            c = s[i]
            if c == '(':
                output.append(''.join(tempchars))
                tempchars.clear()
                middle, endpos = recurseTokenize(i+1)
                output.append(middle)
                i = endpos+1
            elif c == ')':
                output.append(''.join(tempchars))
                return (output, i)
            else:
                tempchars.append(s[i])
                i += 1
        if len(tempchars) > 0:
            output.append(''.join(tempchars))
        return [output, len(s)]

    res, endpos = recurseTokenize(0)

    # Now act on this tokenized string:
    # ['abc', [[['A'], ['B']], 'C']]
    
    print(res)

    class Substr:
        def __init__(self, content, flipbit):
            self.content = content
            self.flipbit = flipbit
        def __repr__(self):
            if self.flipbit == 1:
                return ''.join(['Substr(', str(self.content), ')'])
            else:
                return ''.join(['Substr(', str(self.content[::-1]), ')'])
        def output(self):
            if self.flipbit == 1:
                return self.content
            else:
                return self.content[::-1]
        def __add__(self, other):
            return Substr(self.content[::self.flipbit] + other.content[::other.flipbit],1)

    def recurseAlgebra(obj):
        if type(obj) == str:
            return Substr(obj, 1)
        else: # If not a string, it's of type list
            intermediate = []
            for index, elm in enumerate(obj):
                if type(elm) == list:
                    # Apply recurseAlgebra to deal with sublist
                    for newstr in recurseAlgebra(elm):
                        intermediate.append(newstr)
                else: # It's of type string
                    intermediate.append(Substr(elm, 1))
            # Now the intermediate list should be a collection of strings
            return [Substr(x.content,x.flipbit*-1) for x in intermediate[::-1]]

    output = recurseAlgebra([res])
    return ''.join([s.output() for s in output])

if __name__ == "__main__":
    test = '((abcd(e)fg((hi))jk))'
    res = flipstring(test)
    print(res)
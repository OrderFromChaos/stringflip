def reverseInParentheses(inputString):
    class Substr:
        def __init__(self, content, flipbit):
            self.content = content
            self.flipbit = 1

    # TODO Purposefully hobbled to only work on stuff inside parens; will fix later
    substrs = []
    openparen = []
    for index, char in enumerate(inputString):
        if char == '(':
            openparen.append(index)
        if char == ')':
            substrs.append(Substr(inputString[openparen[-1]+1:index],1)) # No flipping yet
            openparen.pop()

    

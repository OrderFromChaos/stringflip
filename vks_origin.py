import sys

def reverseInParentheses(inputString):
    offsets = []
    index = 0

    for char in inputString:
        if char == '(':
            offsets.append(index + 1);
            index += 1
        elif char == ')':
            begin = offsets[-1]
            end = index
            inputString = inputString[:begin - 1] + inputString[begin:end][::-1] + inputString[end + 1:] # I hate string splices
            offsets.pop(-1)
            index -= 2 # We removed two characters
            index += 1 # Go to the next character as usual
        else:
            index += 1
    return inputString

print(repr(reverseInParentheses(sys.argv[1])))

import sys

d = {
    ')': '(',
    ']': '['
}


def isBracket(text):
    stack = []
    for c in text:
        if c in '([':
            stack.append(c)
        elif c in ')]':
            if stack:
                top = stack.pop()
                if d[c] != top:
                    return False
            else:
                return False
    return len(stack) == 0


lines = []
while True:
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break
    else:
        lines.append(line)
'''
for l in lines:
    if isBracket(l):
        print('yes')
    else:
        print('no')

'''
for l in lines:
    print('yes' if isBracket(l) else 'no')

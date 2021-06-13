import sys
input = sys.stdin.readline
output = sys.stdout.write
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


n = int(input().strip())
lines = [isBracket(input().strip()) for _ in range(n)]

for i in lines:
    print('YES' if i else 'NO')

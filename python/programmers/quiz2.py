def isBracket(text):
    d = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    stack = []
    for c in text:
        if c in '({[':
            stack.append(c)
        elif c in ')}]':
            if stack:
                top = stack.pop()
                if d[c] != top:
                    return False
            else:
                return False
    return len(stack) == 0


def solution(s):
    answer = 0
    for i in range(len(s)):
        if isBracket(s):
            answer += 1
        s += s[0]
        s = s[1:]
    return answer

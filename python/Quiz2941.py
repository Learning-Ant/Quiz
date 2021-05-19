import sys

input = sys.stdin.readline


croatic = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
strInput = input().strip()

for i in croatic:
    strInput = strInput.replace(i, ' ')

print(len(strInput))


'''
스택으로 풀어보려 했지만
왜인지 실패
'''
stack = list(input().strip())

d = {'=': ['c', 'dz', 's', 'z'],
     '-': ['c', 'd'],
     'j': ['l', 'n'],
     }

count = 0
while stack:
    popped = stack.pop()
    if popped in d:
        if popped == '=' and len(stack) > 1 and stack[-2] == 'd':
            stack.pop()
            stack.pop()
        elif len(stack) > 0 and stack[-1] in d[popped]:
            stack.pop()
        count += 1
    else:
        count += 1

print(count)

import sys

input = sys.stdin.readline

n = int(input())

numbers = [int(input()) for _ in range(n)]

stack = []
cmd = []
pointer = 0
for i in range(1, n+1):
    stack.append(i)
    cmd.append('+')
    while stack and stack[-1] == numbers[pointer]:
        stack.pop()
        cmd.append('-')
        pointer += 1

if stack:
    print('NO')
else:
    for i in cmd:
        print(i)

import sys

input = sys.stdin.readline

n = int(input().strip())
stack = []
for i in range(n):
    num = int(input().strip())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

sys.stdout.write(str(sum(stack)))

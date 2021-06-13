import sys

input = sys.stdin.readline


def size():
    print(len(stack))


def pop():
    print(-1 if len(stack) == 0 else stack.pop())


def empty():
    print(1 if len(stack) == 0 else 0)


def top():
    print(-1 if len(stack) == 0 else stack[-1])


n = int(input().strip())
stack = []
functions = {
    'size': size,
    'pop': pop,
    'empty': empty,
    'top': top
}

for _ in range(n):
    command = input().strip().split()
    if command[0] == 'push':
        stack.append(int(command[1]))
    else:
        functions[command[0]]()

'''
93220 KB	2228 ms
'''

import sys
from collections import deque

input = sys.stdin.readline


def size():
  print(len(queue))


def pop():
  print(-1 if len(queue) == 0 else queue.popleft())


def empty():
  print(1 if len(queue) == 0 else 0)


def front():
  print(-1 if len(queue) == 0 else queue[0])

def back():
  print(-1 if len(queue) == 0 else queue[-1])
  

n = int(input().strip())
queue = deque()
functions = {
    'size': size,
    'pop': pop,
    'empty': empty,
    'front': front,
    'back' : back
}

for _ in range(n):
  command = input().strip().split()
  if command[0] == 'push':
      queue.append(int(command[1]))
  else:
      functions[command[0]]()
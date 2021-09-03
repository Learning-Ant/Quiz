'''
31900 KB	160 ms
'''

import sys
from collections import deque
input = sys.stdin.readline

def bfs(v:int, eArr:list, visited:list, queue:deque, cur:int):
  curList = [0] * v
  while queue:
    next = queue.popleft()
    for i in range(v):
      if curList[i] == 0 and eArr[next][i] == 1:
        curList[i] = 1
        visited[cur][i] = 1
        queue.append(i)



v = int(input().strip())
eArr = [list(map(int, input().strip().split())) for _ in range(v)]
visited = [[0] * v for _ in range(v)]
queue = deque()

for i in range(v):
  queue.append(i)
  bfs(v, eArr, visited, queue, i)

for i in visited:
  print(*i)
'''
벽의 위치에 따라 안전구역과 오염구역이 나뉘게 된다.
안전구역이 최대가 되는 벽의 위치를 바로 판단할 방법이 없다.
즉, brute force + dfs(bfs) 로 풀어야 한다는 의미

풀이중
'''

import sys
from collections import deque
input = sys.stdin.readline

def bfs(field:list, y:int, x:int, visited:list):
  queue = deque()
  queue.append()

y, x = map(int, input().split())

original = [list(map(int, input().split())) for _ in range(y)]

copy = original.copy()
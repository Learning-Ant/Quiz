'''
좀.. 너무 브루트포스인데..

다른 풀이들을 보니 그래프 탐색 알고리즘으로도 가능한 듯 하다

34888 KB	6764 ms
'''

import sys
input= sys.stdin.readline

tetro = [
  [(0, 1), (0, 2), (0, 3)],
  [(1, 0), (2, 0), (3, 0)],
  [(1, 1), (1, 0), (0, 1)],
  [(1, 0), (2, 0), (2, 1)],
  [(1, 0), (1, -1), (1, -2)],
  [(-1, 0), (-1, 1), (-1, 2)],
  [(0, 1), (1, 1), (2, 1)],
  [(1, 0), (2, 0), (2, -1)],
  [(1, 0), (1, 1), (1, 2)],
  [(1, 0), (2, 0), (0, 1)],
  [(0, 1), (0, 2), (1, 2)],
  [(1, 0), (1, 1), (2, 1)],
  [(0, -1), (1, -1), (1, -2)],
  [(1, 0), (1, -1), (2, -1)],
  [(0, 1), (1, 1), (1, 2)],
  [(1, 0), (1, -1), (1, 1)],
  [(1, 0), (2, 0), (1, 1)],
  [(0, 1), (1, 1), (0, 2)],
  [(1, 0), (2, 0), (1, -1)]
]

y, x = map(int, input().strip().split())
field = [list(map(int, input().strip().split())) for _ in range(y)]
ans = 0
s = 0
for i in range(y):
  for j in range(x):
    for k in tetro:
      s = field[i][j]
      for l in k:
        ny = i + l[0]
        nx = j + l[1]
        if 0 > ny or ny >= y or 0 > nx or nx >= x:
          break
        s += field[ny][nx]
      ans = max(ans, s)

print(ans)
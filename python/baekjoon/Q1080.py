'''
3X3씩 뒤집기
'''

import sys
input = sys.stdin.readline

def change(row, col, arr):
  for i in range(row, row + 3):
    for j in range(col, col + 3):
      arr[i][j] = 1 - arr[i][j]

n, m = map(int, input().strip().split())

a = [list(map(int, input().strip())) for _ in range(n)]
b = [list(map(int, input().strip())) for _ in range(n)]

cnt = 0

for i in range(n - 2):
  for j in range(m - 2):
    if a[i][j] != b[i][j]:
      change(i, j, a)
      cnt += 1

flag = False
for i in range(n):
  for j in range(m):
    if flag:
      break
    if a[i][j] != b[i][j]:
      flag = True
      break
  if flag: break

if flag:
  cnt = -1

print(cnt)

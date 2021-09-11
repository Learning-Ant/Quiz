'''
간격을 처음부터 더해가면서 테이프 길이 - 1만큼 간격이 채워졌을 때마다
테이프의 개수를 늘려간다

29200 KB	76 ms
'''

import sys
input = sys.stdin.readline

n, l = map(int, input().strip().split())

holes = sorted(list(map(int, input().strip().split())))

cnt = 0
totDiff = 0
curDiff = 0

for i in range(n-1):
  curDiff = (holes[i + 1] - holes[i])
  totDiff += curDiff
  if totDiff > l - 1:
    cnt += 1
    totDiff = 0

print(cnt + 1)


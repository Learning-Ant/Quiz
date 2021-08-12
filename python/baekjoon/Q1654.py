'''
구하고자 하는 길이를 이분탐색으로 찾아가는 문제
29452 KB	108 ms
'''

import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lines = [int(input()) for _ in range(k)]

maxL, minL = max(lines), 1

while minL <= maxL:
  midL = (minL + maxL) // 2
  cnt = sum([i//midL for i in lines])
  if cnt >= n:
    minL = midL + 1
  else :
    maxL = midL - 1

print(maxL)
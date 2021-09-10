'''
29200 KB	72 ms
'''

import sys
input = sys.stdin.readline

n = int(input())

levelScores = [int(input().strip()) for _ in range(n)]
cnt = 0

for i in range(n-1, 0, -1):
  if levelScores[i-1] >= levelScores[i]:
    cnt += levelScores[i-1] - levelScores[i] + 1
    levelScores[i-1] = levelScores[i] - 1

print(cnt)
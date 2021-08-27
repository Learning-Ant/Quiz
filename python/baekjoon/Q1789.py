'''
29200 KB	84 ms
'''

import sys
input = sys.stdin.readline

s = int(input())
cnt = 1
while True:
  if s < cnt:
    cnt -= 1
    break
  else :
    s -= cnt
    cnt += 1

print(cnt)
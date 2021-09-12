'''
29200 KB	72 ms
'''

import sys
input = sys.stdin.readline

l = list(input().strip())
w = input().strip()
n = len(w)
cnt = 0

while True:
  if len(l) < n:    
    break
  if ''.join(l[:n]) == w:
    del l[:n]
    cnt += 1
  else :
    del l[0]

print(cnt)
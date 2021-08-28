'''
33836 KB	180 ms
'''

import sys
input = sys.stdin.readline

n = int(input())
lopes = sorted([ int(input()) for _ in range(n) ])
maxW = n * lopes[0]
for i in range(1, n):
  maxW = max(maxW, (n - i) * lopes[i])

print(maxW)
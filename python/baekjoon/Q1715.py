'''
카드를 섞을 때마다 최소의 카드 개수를 가진 뭉치 둘을 더해야 하는
그리디 알고리즘

32052 KB	272 ms
'''

import sys
import heapq

input = sys.stdin.readline

hq = []

n = int(input().strip())
ans = 0

for _ in range(n):
  heapq.heappush(hq, int(input().strip()))

while n != 1:
  a = heapq.heappop(hq)
  b = heapq.heappop(hq)
  ans += a + b
  heapq.heappush(hq, a + b)
  n -= 1

print(ans)
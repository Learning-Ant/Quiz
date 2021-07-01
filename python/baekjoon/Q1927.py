import sys
import heapq
input = sys.stdin.readline
hq = []

tc = int(input())

for i in range(tc):
    opr = int(input())
    if opr != 0:
        heapq.heappush(hq, opr)
    elif len(hq) == 0:
        print(0)
    else:
        print(heapq.heappop(hq))

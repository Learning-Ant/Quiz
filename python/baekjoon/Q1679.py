'''
34904 KB	264 ms
'''

import sys
from collections import deque

input = sys.stdin.readline

subin, sister = map(int, input().split())
visited = [0] * 100001
visited[subin], visited[sister] = 1, 1

queue = deque()
queue.append([subin, 0])

if subin == sister:
    print(0)
    exit()

while queue:
    cur, t = queue.popleft()
    moveTo = [cur, 1, -1]

    for m in moveTo:
        next = cur + m
        if next == sister:
            print(t+1)
            queue.clear()
            break

        if 0 <= next <= 100000 and visited[next] != 1:
            queue.append([next, t+1])
            visited[next] = 1

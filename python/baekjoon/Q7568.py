import sys

input = sys.stdin.readline

n = int(input())
_list = [tuple(map(int, input().strip().split())) for _ in range(n)]
answer = [1] * n
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if _list[i][0] < _list[j][0] and _list[i][1] < _list[j][1]:
            answer[i] += 1
print(*answer)

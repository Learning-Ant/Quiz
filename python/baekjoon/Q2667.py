'''
    문제에서 굳이 단지번호까지 입력할 필요는 없었지만
    각 단지 번호도 입력할 수 있도록 코드를 구성해보았다.
    하지만 그 성능에 대해서는 좋은지 잘 모르겠다.
    다른 사람들의 경과시간이나 메모리를 비교해보면 상대적으로 높은 자원 소모율을 보이고 있다.
    후에 시간이 된다면 dfs로도 풀어봐야겠다.
'''

from collections import deque

direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def bfs(y, x, visited, direction, length, estate, houseMap):
    count = 0
    queue = deque()
    queue.append((y, x))
    count += 1
    while queue:
        # print(count)
        # print(queue)
        now = queue.popleft()
        visited[now[0]][now[1]] = True
        for d in direction:
            nextY = now[0] + d[0]
            nextX = now[1] + d[1]
            if 0 <= nextY <= length - 1 and 0 <= nextX <= length - 1 and not visited[nextY][nextX] and houseMap[nextY][nextX] == 1 and not (nextY, nextX) in queue:
                houseMap[nextY][nextX] = estate
                queue.append((nextY, nextX))
                count += 1

    return count


n = int(input())

houseMap = [list(map(int, list(input().strip()))) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

estate = 1

result = []

for y in range(n):
    for x in range(n):
        if not visited[y][x] and houseMap[y][x] == 1:
            visited[y][x] = True
            houseMap[y][x] = estate
            result.append(bfs(y, x, visited, direction, n, estate, houseMap))
            estate += 1

result.sort()
print(estate-1)
for i in result:
    print(i)

'''
    dfs로 풀면 BOJ에서는 RecursionError가 발생한다.
    이는 BOJ가 설정한 최대 재귀 깊이가 1000이기때문이며, 임의적으로 최대 재귀 깊이를 설정해주어야 오류가 발생하지 않는다.
    이 문제처럼 연쇄적인 탐색이 필요한 경우엔 dfs보다는 bfs를 사용하는 것이 좋을 것 같다.
'''
import sys

sys.setrecursionlimit(10**6)

def dfs(field, x, y, r, c):
    if x <= -1 or x >= r or y <= -1 or y >= c or field[x][y] != 1:
        return False

    field[x][y] = 2
    dfs(field, x - 1, y, r, c)
    dfs(field, x, y - 1, r, c)
    dfs(field, x + 1, y, r, c)
    dfs(field, x, y + 1, r, c)
    return True


tc = int(input())
result = []
for _ in range(tc):
    count = 0
    r, c, n = map(int, input().split())

    field = [[0] * c for _ in range(r)]

    for _ in range(n):
        x, y = map(int, input().split())
        field[x][y] = 1

    for i in range(r):
        for j in range(c):
            if dfs(field, i, j, r, c):
                count += 1

    result.append(count)
    # for i in field:
    #     print(i)

print("\n".join(map(str, result)))

'''
32976 KB	2616 ms
자원소모가 적지않은 결과를 보인다.
대부분의 사람들이 비슷한 결과를 보이고 있다.
지금까지 풀었던 그래프 순회에 관한 문제들은 순회하려는 field나 data영역들의 크기가 작아
큰 자원 소모율이 일어나지 않았던 것 같다. 하지만 이 문제의 경우에는 최대 300 X 300의 2차원 배열을
테스트 케이스의 수만큼 검사해야한다. 그렇기에 이런 소모율을 보이는 듯하다.
But, 몇몇사람은 훨씬 좋은 효율을 보이고있다. 이런 효율을 극한으로 올릴 방법이 있다는 의미이다.
다른 사람들의 코드를 분석하면서 그에 대해 습득해보도록 해야겠다.
'''

from collections import deque


def bfs(start, dest, n, board):
    queue = deque()
    queue.append(start)
    v = [[-2, 1], [-1, 2], [1, 2], [2, 1],
         [2, -1], [1, -2], [-1, -2], [-2, -1]]
    while queue:
        curY, curX = queue.popleft()
        if curY == dest[0] and curX == dest[1]:
            print(board[curY][curX])
            break
        for next in v:
            nextY = curY + next[0]
            nextX = curX + next[1]
            if 0 <= nextY <= n - 1 and 0 <= nextX <= n - 1 and board[nextY][nextX] == 0:
                board[nextY][nextX] = board[curY][curX] + 1
                queue.append((nextY, nextX))


tc = int(input())
for _ in range(tc):
    n = int(input())
    start = tuple(map(int, input().strip().split()))
    dest = tuple(map(int, input().strip().split()))
    board = [[0] * n for _ in range(n)]
    bfs(start, dest, n, board)

'''
일단 직관적으로 생각했을 때는 여러 조건들을 설정할 수 있도록 함수를 만드는 것이
좋다고 생각이 들긴하는데 이를 응집도의 관점에서 살펴볼 수 있을지 궁금하다.
과연 이런 문제풀이를 위한 함수도 적용이 가능한가?
사실 응집도라는 것 자체가 모듈 내부의 기능적 집중도인 것이니 상관은 없을 것 같긴하다.

우연, 논리, 시간, 절차, 통신, 순차, 기능.

기능으로 갈수록 높음
우연일수록 낮음

응집도는 높을수록 좋음

이와 별개로 다른 답안들을 살펴보니 대부분 색약의 경우 본래의 필드를 변환하거나, 
색약만의 필드를 만드는 경우가 많은 것 같다.

내 생각에는 본래 이미지는 변하지 않고 보는 사람에 따라 변하므로 함수에서 Handling해주는 것이 문제의도에 맞다고 생각해
함수에서 색약인지 아닌지에 따라 다른 값을 낼 수 있도록 설정했다.
저렇게 이미지 자체를 따로 두거나, 이미지를 변경하는 방법도 좋을 듯 하다.

33024 KB	124 ms
'''

import sys
from collections import deque

input = sys.stdin.readline

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def bfs(img: list, n: int, y: int, x: int, weakness: bool, visited: list):
    if visited[y][x] == 1:
        return

    queue = deque()
    queue.append((y, x))
    initColor = img[y][x]

    # 적록색맹일 경우
    if weakness and (initColor == 'R' or initColor == 'G'):
        initColor = set(['R', 'G'])

    visited[y][x] = 1

    while queue:
        cur = queue.popleft()
        for i in range(4):
            nextY = cur[0] + dy[i]
            nextX = cur[1] + dx[i]
            if 0 <= nextY < n and 0 <= nextX < n and visited[nextY][nextX] == 0 and img[nextY][nextX] in initColor:
                queue.append((nextY, nextX))
                visited[nextY][nextX] = 1


n = int(input())
img = [''.join(input().split()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
answer = [0, 0]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(img, n, i, j, False, visited)
            answer[0] += 1

visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(img, n, i, j, True, visited)
            answer[1] += 1


for i in range(2):
    print(answer[i], end=' ')

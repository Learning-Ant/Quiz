import sys
from collections import deque

# tail 제어방법..

input = sys.stdin.readline

queue = deque()

snake = {
    'head': [0, 0],
    'tail': [0, 0]
}
cardinal = [
    [-1, 0],  # N
    [0, 1],  # E
    [1, 0],  # S
    [0, -1]  # W
]

'''
아무것도 없음 : 0
사과 : 1
뱀 : 2
'''
curDir = 1  # D면 +1, L이면 -1
n = int(input())
field = [[0] * n for _ in range(n)]
appleCnt = int(input())
for _ in range(appleCnt):
    y, x = map(int, input().split())
    field[y-1][x-1] = 1

# 뱀 배치
field[0][0] = 2

# 방향 전환 정보
cmdCnt = int(input())
for _ in range(cmdCnt):
    queue.append(input().split())

for i in range(n):
    print(field[i])

print(queue)

time = 0  # 시간

'''
1초 증가 -> 머리 한칸 전진 -> 사과 판단
-> 있으면 꼬리고정, 없으면 꼬리 전진 이전 칸 0으로 전환
이동 가능한지 판단하는 함수 isPossible(필드, 이동방향)
'''


def isPossible(field: list, dir: list, snake: dict, time: int) -> bool:
    nextY = snake['head'][0] + dir[0]
    nextX = snake['head'][1] + dir[1]
    if nextY < 0 or nextY >= n or nextX < 0 or nextX >= n or field[nextY][nextX] == 2:
        print(time+1)
        return False
    return True


cmd = queue.popleft()

while isPossible(field, cardinal[curDir], snake, time):
    print("시간: ", time)
    print(snake)
    if time >= int(cmd[0]):
        print("방향전환")
        curve = cmd[1]
        if curve == 'D':
            curDir = (curDir + 1) % 4
        elif curve == 'L':
            curDir = (curDir - 1) % 4
            print(curDir)
        cmd = queue.popleft()

    curCoord = snake['head']
    nextY = curCoord[0] + cardinal[curDir][0]
    nextX = curCoord[1] + cardinal[curDir][1]
    if field[nextY][nextX] == 1:
        field[nextY][nextX] = 2
        snake['head'] = [nextY, nextX]
    else:
        tailCoord = snake['tail']
        field[tailCoord[0]][tailCoord[1]] = 0
        field[nextY][nextX] = 2
        snake['head'] = [nextY, nextX]
        snake['tail'] = [tailCoord[0]+cardinal[curDir]
                         [0], tailCoord[1]+cardinal[curDir][1]]

    for i in range(n):
        print(field[i])
    time += 1
    print("----------------")

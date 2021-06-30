dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def dfs(y: int, x: int, answer: list):
    if len(answer) == 6:
        return
    else:
        for d in dir:
            nextY = y + d[0]
            nextX = x + d[1]
            if 0 <= nextX <= 4 and 0 <= nextY <= 4:
                answer.append(field[nextY][nextX])
                dfs(nextY, nextX, answer)


field = [list(map(int, input().strip().split())) for _ in range(5)]

answerSet = set()
for i in range(5):
    for j in range(5):
        answer = [field[i][j]]
        dfs(i, j, answer)
        answerSet.add(int("".join(map(str, answer))))

print(answerSet)

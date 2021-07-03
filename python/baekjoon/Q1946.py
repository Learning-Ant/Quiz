# 먼저 두 시험 중 하나라도 1등이면 무조건 합격
# 2중 for문은 n^2의 시간복잡도로 n이 100,000인 이 문제의 경우
# 시간초과가 뜰 수 밖에 없다.
# 먼저 정렬을 수행한 후 하나의 for문으로 문제를 해결한다.
'''
69036 KB	6216 ms
'''

import sys
input = sys.stdin.readline


def sol(rankList: list):
    answer = []
    maxA = 100001
    maxB = 100001

    for i in rankList:
        if i[0] < maxA and i[1] < maxB:
            answer.append(i)
            maxA = i[0]
            maxB = i[1]
        elif i[0] < maxA and i[1] > maxB:
            answer.append(i)
            maxA = i[0]
        elif i[0] > maxA and i[1] < maxB:
            answer.append(i)
            maxB = i[1]
    print(answer)
    return len(answer)


tc = int(input())
for _ in range(tc):
    count = int(input())
    rankList = [list(map(int, input().strip().split())) for _ in range(count)]
    rankList.sort()
    print(sol(rankList))

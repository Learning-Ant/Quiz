'''
Q1992, Q2630과 같은 문제

67632 KB	5640 ms

delta값이 1일 경우 바로 return하는 코드를 삽입하면

67648 KB	3564 ms
'''
import sys
input = sys.stdin.readline


def dc(data: list, row: int, col: int, delta: int, count: list):
    val = data[row][col]
    if delta == 1:
        count[val] += 1
        return
    for i in range(row, row+delta):
        for j in range(col, col+delta):
            if data[i][j] != val:
                ddelta = delta // 3
                for ii in range(3):
                    for jj in range(3):
                        dc(data, row + ii * ddelta, col +
                           jj * ddelta, ddelta, count)
                return

    count[val] += 1


n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
count = [0, 0, 0]
dc(paper, 0, 0, n, count)  # devision conquer

print(count[-1])
print(count[0])
print(count[1])

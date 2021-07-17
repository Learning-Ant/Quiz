'''
나뉘어지면 괄호로 묶인다.

29452 KB	80 ms
'''
import sys
input = sys.stdin.readline


def qTree(data: list, result: list, row: int, col: int, delta: int):
    curData = data[row][col]
    for i in range(row, row + delta):
        for j in range(col, col + delta):
            if curData != data[i][j]:
                # 일치하지 않으면 분할하면서 괄호로 묶어준다.
                result.append("(")
                ddelta = delta // 2
                # loop 분할방법
                # row devide 2
                for ii in range(2):
                    # col devide 2
                    for jj in range(2):
                        qTree(data, result, row + ii * ddelta,
                              col + jj * ddelta, ddelta)
                # 분할 후 재귀호출했으므로 괄호로 닫아준다.
                result.append(")")
                return
    result.append(str(curData))


n = int(input())
data = [list(map(int, list(input().strip()))) for _ in range(n)]

# print(data)
result = []
qTree(data, result, 0, 0, n)
print("".join(result))

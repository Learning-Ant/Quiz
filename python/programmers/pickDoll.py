def pickUp(board, colNum):
    for rows in board:
        if rows[colNum] != 0:
            print("pick up :", rows[colNum])
            pickVal = rows[colNum]
            rows[colNum] = 0
            return pickVal
    print("don't pick up anything")
    return 0


def pickPop(stack, pickVal, count):
    last = stack.pop()
    if last == pickVal:
        print("Pop pickVal :", last, pickVal)
        print(stack)
        return 2
    else:
        print("append last :", last)
        stack.append(last)

    print("append new pick :", pickVal)
    stack.append(pickVal)
    print(stack)
    return 0


def solution(board, moves):
    stack = []
    count = 0
    for i in moves:
        print("---------pick at", i, "---------")
        pick = pickUp(board, i-1)
        if pick != 0:
            if stack:
                count += pickPop(stack, pick, count)
            else:
                stack.append(pick)

    print(stack)
    return count


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(board)
print(solution(board, moves))
print(board)
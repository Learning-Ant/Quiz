'''
N X N행렬에 N개의 퀸

부분해를 재귀적으로 찾으면서 n개의 줄을 완성했을 경우에만
count를 올려 총 몇 가지의 답을 가지는지 찾는 방법으로 구현한다.

시간을 줄이기 위해선 이미 배치를 끝낸 다음의 row부터 검사를 시작해야한다.
'''

import sys
input = sys.stdin.readline

# Queen을 놓을 수 있는 경우의 수를 backtracking으로 세기
def bt(chess:list, row:int, nQ:int, sCnt:int):
  if not isPossible(chess, row):
    print('fail')
    return
  
  if row == nQ - 1:
    sCnt += 1
    print(sCnt)
  else :
    for i in range(nQ):
      print('row:',row+1)
      chess[row + 1] = i
      bt(chess, row + 1, nQ, sCnt)

# 놓을 수 있는 자리인지 판단
def isPossible(chess:list, row:int)->bool:
  curRow = 0
  while curRow < row:
    if chess[row] == chess[curRow] or abs(chess[row] - chess[curRow]) == abs(row - curRow):
      return False
    curRow += 1
  return True

nQ = int(input())

chess = [0] * nQ
sCnt = 0

for i in range(nQ):
  chess[0] = i;
  bt(chess, 0, nQ, sCnt)

print(sCnt)
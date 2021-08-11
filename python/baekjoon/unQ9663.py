'''
N X N행렬에 N개의 퀸

부분해를 재귀적으로 찾으면서 n개의 줄을 완성했을 경우에만
count를 올려 총 몇 가지의 답을 가지는지 찾는 방법으로 구현한다.
'''

import sys
input = sys.stdin.readline

# Queen을 놓을 수 있는 경우의 수를 backtracking으로 세기
def backtracking(chess:list, row:int, n:int, sCnt:int):
  if isPossible(chess, row):
    return
    

# 놓을 수 있는 자리인지 판단
def isPossible(chess:list, row:int)->bool:
  if 1 == 1 :
    return True

n = int(input())

chess = []


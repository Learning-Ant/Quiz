'''
음.. itertools 모듈을 사용하지 않고 해보려했는데
모듈을 사용하지 않은 다른 사람들처럼 성능이 나오지 않는다.

다른 사람들의 코드를 보고 분석이 좀 필요할 것 같다.
29200 KB	188 ms
'''

import sys

input = sys.stdin.readline

def chk(caseList:list, moem:list)->bool:
  moCnt = 0
  jaCnt = 0
  for i in caseList:
    if i in moem:
      moCnt += 1
    else :
      jaCnt += 1

  if moCnt >= 1 and jaCnt >= 2:
    return True
  else :
    return False
      
def printPw(cnt:int, pwList:list, caseList:list, maxL:int, moem):
  if cnt == maxL:
    if chk(caseList, moem):
      print(''.join(caseList))
    return

  for i in range(len(pwList)):
    if pwList[i] not in caseList:
      if len(caseList) == 0:
        caseList.append(pwList[i])
        printPw(cnt+1, pwList, caseList, maxL, moem)
        caseList.pop()
      elif len(caseList) > 0 and caseList[-1] < pwList[i]:
        caseList.append(pwList[i])
        printPw(cnt+1, pwList, caseList, maxL, moem)
        caseList.pop()


moem = set(('a', 'e', 'i', 'o', 'u'))
l, c = map(int, input().split())
pwList = input().split()
pwList.sort()

caseList = []

print(pwList)


printPw(0, pwList, caseList, l, moem)
'''
우선 6이 세 번 '이상' '연속'으로 들어가는 수를 찾아야하는 문제
처음 생각 할 때 6이 세 번'이상' 들어가기만 하면 되는 줄 알고 풀었다가 오답처리가 되었다.

좀더 문제를 꼼꼼히 보는 습관을 들이도록 한다.

시간을 더 줄일 방법
1. math를 사용하지 않고 다른 방법으로 풀이
2. 문자열에 in을 사용 할 수 있음을 이용한 방법

31312 KB	3724 ms
'''

import sys
import math
input = sys.stdin.readline

def chkNum(num:int):
  cnt = 0

  for i in range(int(math.log10(num)+1)):
    if num % 10 == 6:
      cnt += 1
    else :
      cnt = 0

    if cnt == 3:
      break;

    num //= 10

  if cnt == 3 :
    return True
  else :
    return False


count = 0
temp = 666

n = int(input().strip())

while True:
  if chkNum(temp):
    count += 1
  
  if count == n:
    break
  temp += 1

print(temp)
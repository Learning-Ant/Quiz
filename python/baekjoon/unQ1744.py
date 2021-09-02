'''
너무 단순하게 생각한 풀이

여러 경우를 생각하고 해당 경우에 맞는 연산을 적용할 수 있도록 해야한다.

지금의 코드는 단순하게 가장 큰 양수부터 두개씩 짝지어 곱해 더해주는 과정일 뿐

'''

import sys
input = sys.stdin.readline

n = int(input().strip())

nList = sorted([int(input().strip()) for _ in range(n)])

print(nList)
ans = 0



while True:
  if len(nList) <= 1:
    if len(nList) == 1 :
      ans += nList[0]
    break

  a = nList.pop()
  b = nList.pop()

  ans += max(a * b, a + b)
  # print(ans)
  # print(nList)
  

print(ans)
  
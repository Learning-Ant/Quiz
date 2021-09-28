'''
너무 단순하게 생각한 풀이

여러 경우를 생각하고 해당 경우에 맞는 연산을 적용할 수 있도록 해야한다.

지금의 코드는 단순하게 가장 큰 양수부터 두개씩 짝지어 곱해 더해주는 과정일 뿐

21.09.28
최대를 구하기 위해서는 정렬을 진행한 후
음수들은 가장 작은 수부터 2개씩 곱해주고,
양수들은 가장 큰 수부터 2개씩 곱해준다.
그렇게 곱해주며 없애면 양수부분, 음수부분 각각 원소가 하나씩 남는 경우가 있는데
이 수들은 그냥 더해주도록 한다.

1이 총 입력 값 중 두 개 이상일 경우를 생각하면 두 1은 곱해도 1이므로
더해줄 때 최대값이 나오게 된다.

지금의 코드는 2개 남았을 경우를 따로 예외로 설정했지만,
애초에 입력을 받을 때 1은 바로 답 변수에 더해주고 리스트에 삽입하지 않는 방식으로도
필터링이 가능하다.

29200 KB	84 ms
'''

import sys
input = sys.stdin.readline

n = int(input().strip())

nList = sorted([int(input().strip()) for _ in range(n)])
idx = 0
for i in range(n):
  if nList[i] > 0:
    idx = i
    break
ans = 0
minus = sorted(nList[:idx], reverse=True)
plus = nList[idx:]

while True:
  if not (minus or plus) :
    break
  if len(minus) > 1:
    ans += (minus.pop() * minus.pop())
  elif len(minus) == 1:
    ans += minus.pop()
  if len(plus) > 1:
    a, b= plus.pop(), plus.pop()
    if b == 1:
      ans += (a + b)
    else :
      ans += (a * b)
  elif len(plus) == 1:
    ans += plus.pop()

print(ans)




# ----------------------------------------------------
# while True:
#   if len(nList) <= 1:
#     if len(nList) == 1 :
#       ans += nList[0]
#     break

#   a = nList.pop()
#   b = nList.pop()

#   ans += max(a * b, a + b)
#   # print(ans)
#   # print(nList)
  

# print(ans)
  
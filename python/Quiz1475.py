import sys
input = sys.stdin.readline
# 한 세트 구성
nSet = [i if i != 6 else i+3 for i in range(10)]
# 현재 가진 구성품
haveSet = []
# 필요 세트 수
setCount = 0
# 입력 받을 때 6과 9 구분제거
num = list(map(int, input().strip().replace('6', '9')))

# num이 다 제거 될 때까지 반복
while num:
    if num[-1] in haveSet:
        haveSet.remove(num[-1])  # 소모 구성품 제거
        num.pop()               # 만족한 숫자 제거
    else:
        haveSet += nSet         # 구성품이 없으면 한 세트 추가
        setCount += 1           # 세트 카운트 증가

print(setCount)

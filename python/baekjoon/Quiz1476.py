import sys
input = sys.stdin.readline
# 1년이 지나면 각 자리수는 1씩 증가한다.
# 즉 입력된 자리수를 각자 1씩 감소시키며 환산한 연도를 1씩 증가시킬 때
# 각 자리수가 모두 1, 1, 1이 될 때 그 연도를 알 수 있다.
e, s, m = map(int, input().strip().split())
ans = 1
while True:
    if e == 1 and s == 1 and m == 1:
        break

    e -= 1
    if e < 1:
        e = 15
    s -= 1
    if s < 1:
        s = 28
    m -= 1
    if m < 1:
        m = 19
    ans += 1

print(ans)

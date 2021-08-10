'''
최초 생각한의 경우 가장 처음의 체스판 색깔을 바꿀 경우를 생각하지 않았다
예를 들어 B로 시작하는데 W로 바꾸는 경우에 Color Change Cnt가 더 작을 수도 있음을 고려치 못했다.
그렇기에 무조건 두가지 경우를 모두 고려해 주어야 한다.
거기까지 Brute Force를 고려해야 하는 문제였다.

좀 더 다듬는다면 아마 이 두 경우를 미리 변수로 만들어 둔 후 비교하도록 할 수 있겠다.
+ cnt를 할 때 따로 함수를 만들어 cnt를 증가시키거나, 비교하는 방법을 좀 더 깔끔하게 바꿀 수도 있을 것 같다.

29200 KB	160 ms
'''

import sys

input = sys.stdin.readline

m, n = map(int, input().split())

field = [[1 if i == 'B' else 0 for i in input()] for _ in range(m)]

'''
1. 
배열을 8x8씩 순회하면서
첫 색깔을 기억하고, 시작 자리의 인덱스의 짝수 판별 후 
색을 바꿔야하는 경우 counting
그 중 가장 작은 경우의 chainging count 출력
2. 
먼저 정답 체스판을 생성해 둔 후 바꿔야 하는 횟수 counting

여기서 checking function을 따로 제작하느냐 마느냐.
'''

# def printChess(field, y, x):
#     print('--------')
#     for i in range(8):
#         for j in range(8):
#             print( 'B' if field[y+i][x+j] == 1 else 'W', end=' ')
#         print()
#     print('--------')
    

count = 0
answer = m * n
for curM in range(m-7):
    for curN in range(n-7):
        for k in range(2):
            first = (field[curM][curN] + k) % 2
            count = 0
            # printChess(field, curM, curN)
            for i in range(8):
                flag = (i % 2 == 0)  # True = even, False = odd
                for j in range(8):
                    if flag:
                        if j % 2 == 0 and first != field[curM+i][curN+j]:
                            count += 1
                        elif j % 2 == 1 and first == field[curM+i][curN+j]:
                            count += 1
                    else :
                        if j % 2 == 0 and first == field[curM+i][curN+j]:
                            count += 1
                        elif j % 2 == 1 and first != field[curM+i][curN+j]:
                            count += 1
            answer = min(answer, count)

print(answer)

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

count = 0
answer = 65
for curM in range(m-8):
    for curN in range(n-8):
        first = field[curM][curN]
        count = 0
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

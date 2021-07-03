'''
29200 KB	80 ms
굳이 아래처럼 할 필요없이 입력받은 문자열로부터 다른 문자가 나오는 순간들을 모두 세어주고
2로 나눠주면 답이 나온다.
'''
import sys
input = sys.stdin.readline


def countNum(arr: list):
    answer = 0
    for i in arr:
        if i != '':
            answer += 1
    return answer


arr = input().strip()
# print(arr.count(''))
list0 = arr.split('1')
list1 = arr.split('0')
count0 = countNum(list0)
count1 = countNum(list1)

print(count0 if count0 < count1 else count1)

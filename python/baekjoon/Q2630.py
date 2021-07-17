'''
상당히 긴 코드가 작성된 것 같다.
줄이기 위한 방법은 dc함수에 전달하는 arr를 slicing된 arr가 아닌 본 함수를 받고,
slicing 작업이 아닌 indexing을 통해 분할 접근할 수 있도록 바꾸는 것과,
따로 chk함수를 통해 분할 해야하는지 판단하는 방법이 아닌
dc함수에서 배열과 시작 index를 받고 시작 index의 색을 저장해 둔 후
loop로 색을 비교해가며 다른 색을 만났을 때 재귀적으로 dc를 호출해 검사하는 방법을 사용한다면
최소 반정도의 코드길이를 줄일 수 있을 듯하다.

29200 KB	84 ms
'''

import sys
input = sys.stdin.readline

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]


def slice2d(arr: list, start: list, end: list) -> list:
    answer = []
    for i in range(start[0], end[0] + 1):
        answer.append(arr[i][start[1]:end[1]+1])
    return answer


def chk(arr: list) -> bool:
    ns = arr[0][0]
    l = len(arr)
    for i in range(l):
        for j in range(l):
            if arr[i][j] != ns:
                return True
    return False

# return 조건


def dc(arr: list, answer: list):
    ns = arr[0][0]
    l = len(arr)
    if(l <= 2):
        if chk(arr):
            for i in range(l):
                for j in range(l):
                    answer[arr[i][j]] += 1
        else:
            answer[ns] += 1
        #print("----l <= 2----")
        # print(arr)
        return
    else:
        if chk(arr):
            # l은 짝수
            # 다음 Y는
            nextL = l // 2
            dc(slice2d(arr, [0, 0], [nextL-1, nextL-1]), answer)
            dc(slice2d(arr, [0, nextL], [nextL-1, l-1]), answer)
            dc(slice2d(arr, [nextL, 0], [l-1, nextL-1]), answer)
            dc(slice2d(arr, [nextL, nextL], [l-1, l-1]), answer)
        else:
            answer[ns] += 1
            return


answer = [0, 0]
dc(paper, answer)
print("\n".join(list(map(str, answer))))

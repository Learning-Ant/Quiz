import heapq as hq
import sys

input = sys.stdin.readline

testCase = int(input().strip())
answer = []


def heapPop(heapList):
    heapList[0], heapList[-1] = heapList[-1], heapList[0]
    popped = heapList.pop()


for _ in range(testCase):
    heap = []
    count, n = map(int, input().strip().split())

    nums = list(map(int, input().strip().split()))

    for i in range(count):
        hq.heappush(heap, [-nums[i], -i])

    print(heap)
    order = 0
    while True:
        a = hq.heappop(heap)[1]
        print(heap)
        order += 1
        if a == n:

            answer.append(order)
            break
print(answer)
# for ans in answer:
#     print(ans)

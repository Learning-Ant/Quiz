import sys
input = sys.stdin.readline
tc = int(input())
# heapq로는 안될 듯하다.
'''
import heapq
answer = []
for _ in range(tc):
    count, n = map(int, input().strip().split())
    q = []
    priority = list(map(int, input().strip().split()))
    for i in range(count):
        heapq.heappush(q, (-priority[i], -i))

    print(q)
    cnt = 0
    while q:
        cnt += 1
        if heapq.heappop(q)[1] == -n:
            print(cnt)
            answer.append(cnt)
            break

print(answer)
#print('\n'.join(list(map(str, answer))))
'''
answer = []
for _ in range(tc):
    count, n = map(int, input().strip().split())
    priority = list(map(int, input().strip().split()))
    q = []
    for i in range(count):
        q.append((priority[i], i))

    print(q)
    cnt = 0
    while q:
        popped = q.pop(0)
        print(popped)
        if popped[0] == max(priority):
            cnt += 1

            if popped[1] == n:
                answer.append(cnt)
                break
            else:
                priority.remove(popped[0])
        else:
            q.append(popped)

print('\n'.join(list(map(str, answer))))

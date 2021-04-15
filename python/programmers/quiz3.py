def solution(a, edges):
    if sum(a) != 0:
        return -1

    list = [[a[i] if i == j else 0 for i in range(
        len(a))] for j in range(len(a))]

    for i in range(len(edges)):
        list[edges[i][0]][edges[i][1]] = 1

    for i in range(len(list)):

    answer = 0

    return answer


a = [-5, 0, 2, 1, 2]
edges = [[0, 1], [3, 4], [2, 3], [0, 3]]

list = [[a[i] if i == j else 0 for i in range(len(a))] for j in range(len(a))]

for i in range(len(edges)):
    list[edges[i][0]][edges[i][1]] = 1


print(list)

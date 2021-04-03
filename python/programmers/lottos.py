def solution(lottos, win_nums):
    answer = [6, 6]
    rank = 6
    l = set(lottos)
    l.pop()

    for i in l:
        if win_nums.count(i):
            win_nums.pop(i)
    if len(win_nums) < answer[1]:
        answer[1] = len(win_nums)
    zeroC = rank - len(set(lottos))
    answer[0] = answer[1] - zeroC

    return answer


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

print(solution(lottos, win_nums))

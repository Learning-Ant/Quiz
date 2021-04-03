def solution(bridge_length, weight, truck_weights):
    answer = 1
    passSec = 0
    bridge = []
    passed = []
    truckCount = len(truck_weights)
    while len(passed) != truckCount:
        answer += 1
        passSec += 1
        if len(truck_weights) != 0 and sum(bridge) + truck_weights[0] <= weight:
            bridge.insert(0, truck_weights.pop(0))
            print(bridge)

        if passSec == bridge_length:
            print(passSec)
            passSec = 0
            print(passSec)
            passed.append(bridge.pop())
            print(bridge)
        else:
            continue
    return answer


print(solution(100, 100, [100]))

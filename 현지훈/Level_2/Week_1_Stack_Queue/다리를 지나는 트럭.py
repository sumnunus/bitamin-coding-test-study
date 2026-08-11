from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque() # bridge 위에 올라간 트럭들
    truck_idx = 0

    while truck_idx < len(truck_weights):
        answer += 1

        # 현재 시간에 다리 위의 트럭이 빠져나간다면 빠져나감
        if bridge and answer >= bridge[0][1]:
            truck, _ = bridge.popleft()
            weight += truck

        truck = truck_weights[truck_idx]

        # 트럭이 다리 위에 올라갈 수 있다면 올라감.
        if truck <= weight:
            bridge.append((truck, answer + bridge_length))
            weight -= truck
            truck_idx += 1

        # 트럭이 다리 위에 올라갈 수 없다면 앞선 트럭이 빠져나올 시간까지 기다림
        else:
            answer = bridge[0][1] - 1

    return bridge[-1][1]


bridge_length_input = 2
weight_input = 10
truck_weights_input = [7, 4, 5, 6]

print(solution(bridge_length_input, weight_input, truck_weights_input))
from collections import deque


def solution(num_list, n):
    answer = []
    num_queue = deque(num_list)

    for _ in range(n):
        num_queue.append(num_queue.popleft())

    answer = list(num_queue)

    return answer


num_list_input = [2, 1, 6]
n_input = 1

print(solution(num_list_input, n_input))
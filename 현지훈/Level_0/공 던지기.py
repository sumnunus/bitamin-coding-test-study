from collections import deque


def solution(numbers, k):
    answer = 0
    queue = deque(numbers)

    for _ in range(k-1):
        queue.rotate(-2)

    answer = queue[0]

    return answer


numbers_input = [1, 2, 3, 4, 5, 6]
k_input = 5

print(solution(numbers_input, k_input))
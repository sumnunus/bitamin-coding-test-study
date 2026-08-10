import heapq


def solution(array, commands):
    answer = []

    for i, j, k in commands:
        array_hq = array[i-1:j]
        heapq.heapify(array_hq)

        for _ in range(k-1):
            heapq.heappop(array_hq)

        answer.append(heapq.heappop(array_hq))

    return answer


array_input = [1, 5, 2, 6, 3, 7, 4]
commands_input = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array_input, commands_input))
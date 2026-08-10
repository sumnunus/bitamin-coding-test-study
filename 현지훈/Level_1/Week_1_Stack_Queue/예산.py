import heapq


def solution(d, budget):
    answer = 0
    heapq.heapify(d)
    cost = 0

    while True:
        if len(d) == 0:
            break

        cost += heapq.heappop(d)

        if cost > budget:
            break
        else:
            answer += 1

    return answer


d_input = [2,2,3,3]
budget_input = 10

print(solution(d_input, budget_input))
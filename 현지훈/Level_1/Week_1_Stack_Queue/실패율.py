import heapq


def solution(N, stages):
    answer = []
    stage_fail = []
    challenger = len(stages)
    user_count = {i:0 for i in range(1, N+2)}

    for stage in stages:
        user_count[stage] += 1

    for i in range(1, N+1):
        if challenger == 0:
            heapq.heappush(stage_fail, (0, i))
        else:
            heapq.heappush(stage_fail, (-user_count[i]/challenger, i))
            challenger -= user_count[i]

    for _ in range(N):
        answer.append(heapq.heappop(stage_fail)[1])

    return answer


N_input = 5
stages_input = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N_input, stages_input))
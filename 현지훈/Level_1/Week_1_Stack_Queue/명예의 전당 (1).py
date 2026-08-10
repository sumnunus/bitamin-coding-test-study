import heapq


def solution(k, score):
    answer = []
    top_score = []

    # 가수의 점수를 가져옴
    for s in score:
        # 만약 현재 가수의 점수가 명예의 전당 최저점보다 낮고, 이미 명예의 전당이 다 찼다면 넘어가기
        if len(top_score) == k and answer[-1] >= s:
            answer.append(top_score[0])
            continue

        heapq.heappush(top_score, s)

        # 만약 명예의 전당에 k+1개의 점수가 올라가 있다면 가장 낮은 점수를 빼냄.
        if len(top_score) > k:
            heapq.heappop(top_score)

        # 현재 명예의 전당에 올라간 점수들 중 최소 점수를 가져옴.
        answer.append(top_score[0])

    return answer


k_input = 3
score_input = [10, 100, 20, 150, 1, 100, 200]

print(solution(k_input, score_input))
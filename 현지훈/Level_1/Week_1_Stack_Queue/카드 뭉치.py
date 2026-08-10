from collections import deque


def solution(cards1, cards2, goal):
    answer = 'Yes'

    # 각 list를 queue로 변환
    cards1_queue = deque(cards1)
    cards2_queue = deque(cards2)
    goal_queue = deque(goal)

    # 목표 문장을 만들 때까지
    while goal_queue:
        goal_word = goal_queue.popleft()

        # card1에 해당 단어가 있다면
        if cards1_queue and cards1_queue[0] == goal_word:
            cards1_queue.popleft()
        # card2에 해당 단어가 있다면
        elif cards2_queue and cards2_queue[0] == goal_word:
            cards2_queue.popleft()
        # 만들 수 없다면
        else:
            answer = 'No'
            break

    return answer


cards1_input = ["i", "water", "drink"]
cards2_input = ["want", "to"]
goal_input = ["i", "want", "to", "drink", "water"]

print(solution(cards1_input, cards2_input, goal_input))
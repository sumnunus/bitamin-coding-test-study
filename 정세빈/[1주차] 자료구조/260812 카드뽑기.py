from collections import deque


def solution(cards1, cards2, goal):
    answer = ''
    sentence = []
    a = deque(cards1)
    b = deque(cards2)
    for i in range(len(goal)):
        if a and a[0] == goal[i]:
            sentence.append(a.popleft())
        elif b and b[0] == goal[i]:
            sentence.append(b.popleft())    
    if sentence == goal: 
        answer = "Yes"
    else:   
        answer = "No"
    return answer

print(solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))
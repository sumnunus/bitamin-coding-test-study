#cards1 0번 단어 -> 다음은 cards1의 1번 단어 이거나 cards2의 0번 단어
#cards2 0번 단어 -> 다음은 cards2의 1번 단어 이거나 cards1의 0번 단어

from collections import deque

def solution(cards1, cards2, goal):
    q = deque(goal)
    c1 = deque(cards1)
    c2 = deque(cards2)
    answer = 'Yes'  
    
    while q:
        sample = q.popleft()
        if c1 and c1[0] == sample:
            c1.popleft()
            
        elif c2 and c2[0] == sample:
            c2.popleft()
        
        else:
            answer = 'No'
            break      
    return answer
from collections import deque

def solution(A, B):
    AA = deque(list(A))
    BB = deque(list(B))
    answer = 0
    
    for i in range(0,len(AA)+1):
        if AA == BB:
            answer = i
            break
        else:
            AA.rotate(1)
    if AA != BB:
        return -1
        
    return answer
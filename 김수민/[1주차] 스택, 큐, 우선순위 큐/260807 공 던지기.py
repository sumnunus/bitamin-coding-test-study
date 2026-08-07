from collections import deque

def solution(numbers, k):
    q = deque(numbers)
    answer = 0
    q.rotate(-((k-1)*2))
    answer = q.popleft()
    return answer
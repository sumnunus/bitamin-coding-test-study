from collections import deque

def solution(num_list, n):
    num_list = deque(num_list)
    num_list.rotate(-n)
    answer = list(num_list)
    return answer
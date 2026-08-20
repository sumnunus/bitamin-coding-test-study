#구슬의 개수 balls -> n
#친구들에게 나누어 줄 구슬 개수 share -> m
#n! / (n-m)! x m!
import math

def solution(balls, share):
    answer = math.factorial(balls)/(math.factorial(balls-share) * math.factorial(share))
    return answer
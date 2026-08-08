def solution(s):
    answer = 0
    arr = s.split()
    last = 0

    for i in arr:
        if 'Z' in i:
            answer -= last
        else:
            last = int(i)
            answer += last

    return answer


s = "1 2 Z 3"

print(solution(s))
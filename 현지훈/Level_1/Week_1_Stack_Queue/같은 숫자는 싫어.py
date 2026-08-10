def solution(arr):
    answer = []

    for s in arr:
        if len(answer) == 0 or answer[-1] != s:
            answer.append(s)

    return answer


arr_input = [1,1,3,3,0,1,1]

print(solution(arr_input))
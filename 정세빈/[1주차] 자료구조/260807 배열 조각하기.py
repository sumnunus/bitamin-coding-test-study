def solution(arr, query):
    answer = []
    answer = arr
    for i in range(len(query)):
        if i%2==0:
            answer = answer[:(query[i]+1)]
        else:
            answer = answer[query[i]:]
    return answer

print(solution([0, 1, 2, 3, 4, 5],[4, 1, 2]))

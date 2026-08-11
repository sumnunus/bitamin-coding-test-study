def solution(arr, query):
    answer = []
    
    for i,p in list(enumerate(query)):
        if (i%2 == 0) :
            arr = arr[:p+1]
        else:
            arr = arr[p:]
    answer = arr
    return answer
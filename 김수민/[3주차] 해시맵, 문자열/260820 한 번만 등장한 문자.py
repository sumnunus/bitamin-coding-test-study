from collections import Counter

def solution(s):
    answer = ''
    cnt = Counter(s)
    # Counter({"a": 3, "n": 2, "b": 1})
    for k, v in cnt.items():
        if v == 1:
            answer += k  
    sorted_list = sorted(answer)  
    result = "".join(sorted_list)  
    return result
def solution(s):
    answer = 0
    previous = 0
    
    for token in s.split():
        if token == "Z":
            answer -= previous
            
        
        else:
            number = int(token)
            answer += number
            previous = number
    return answer
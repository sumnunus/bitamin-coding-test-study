def solution(s):
    stk = []
    for x in s.split():
        if x == "Z":
            stk.pop()
        else:
            stk.append(int(x))
    return sum(stk)
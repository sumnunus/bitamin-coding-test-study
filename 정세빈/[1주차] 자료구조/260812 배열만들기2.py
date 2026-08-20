def solution(arr):
    stk = []
    for x in arr:
        while stk and stk[-1] >= x:
            stk.pop()
        stk.append(x)
    return stk
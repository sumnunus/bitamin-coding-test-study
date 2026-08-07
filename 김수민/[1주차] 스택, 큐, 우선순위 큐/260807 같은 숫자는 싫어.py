#연속적으로 나타나는 숫자는 '하나'만 남기고 전부 제거 / 순서는 유지

def solution(arr):
    answer = []
    answer.append(arr[0])
    for a in arr[1:]:
        if answer[-1] == a:
            continue
        else:
            answer.append(a)
    return answer
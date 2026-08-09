def solution(A, B):
    answer = 0
    for i in range(len(A)):
        if A==B:
            return i
        A = A[len(A)-1:]+A[:len(A)-1]
    return -1
print(solution("hello","ohell"))
print(solution("apple","elppa"))
print(solution("atat","tata"))
print(solution("abc","abc"))


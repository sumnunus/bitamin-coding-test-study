#ineq -> <, >
#eq -> =, !
#조건 맞으면 1 return
#아니면 0 return

def solution(ineq, eq, n, m):
    if ineq == '<' and eq == '=':
        return int(n <= m)
    elif ineq == '<' and eq == '!':
        return int(n < m)
    elif ineq == '>' and eq == '=':
        return int(n >= m)
    elif ineq == '>' and eq == '!':
        return int(n > m)
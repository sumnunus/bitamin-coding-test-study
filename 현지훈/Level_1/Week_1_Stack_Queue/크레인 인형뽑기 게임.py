def solution(board, moves):
    answer = 0
    bowl = []

    for y in moves:
        y -= 1
        for x in range(len(board)):
            if board[x][y] != 0:
                if len(bowl) > 0 and bowl[-1] == board[x][y]:
                    bowl.pop()
                    answer += 2

                else:
                    bowl.append(board[x][y])

                board[x][y] = 0
                break

    return answer


board_input = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves_input = [1,5,3,5,1,2,1,4]

print(solution(board_input, moves_input))
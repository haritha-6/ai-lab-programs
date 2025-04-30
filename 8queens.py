N = 8

def print_solution(board):
    for row in board:
        line = ""
        for cell in row:
            if cell == 1:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

def is_safe(board, row, col):
    
    for i in range(row):
        if board[i][col] == 1:
            return False

    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

   
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, row):
    if row >= N:
        print_solution(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_nqueens(board, row + 1):
                return True
            board[row][col] = 0 

    return False

board = [[0 for _ in range(N)] for _ in range(N)]

if not solve_nqueens(board, 0):
    print("No solution found.")

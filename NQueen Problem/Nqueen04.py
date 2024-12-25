def printSolution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()

def isSafe(board, row, col, N):
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solveNQueensUtil(board, row, N):
    if row == N:  # Base case: all queens are placed
        printSolution(board)
        return

    for col in range(N):  # Try all columns
        if isSafe(board, row, col, N):
            board[row][col] = 1  # Place the queen
            solveNQueensUtil(board, row + 1, N)  # Recur for the next row
            board[row][col] = 0  # Backtrack

def solveNQueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]  # Initialize the board
    solveNQueensUtil(board, 0, N)  # Start from the first row

# Example: Solve for 4-Queens
# solveNQueens(4)
# solveNQueens(8)
solveNQueens(3)
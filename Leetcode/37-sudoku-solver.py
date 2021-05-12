class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        Backtracking solution that iterates all possible combinations and stops
        recursing when a board is invalid
        """
        self.dfs(board)
        return board

    def dfs(self, board):
        i, j = self.nextIncomplete(board)
        if i == -1 and j == -1: return True
        for n in range(1, 10):
            if self.isValid(board, i, j, str(n)):
                board[i][j] = str(n)
                if self.dfs(board): return True
                board[i][j] = '.'
        return False

    def nextIncomplete(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': return (i, j) 
        return (-1, -1)

    def isValid(self, board, row, col, n):
        # Check if the column is valid
        for i in range(9):
            if board[i][col] == n:
                return False 

        # Check if row is valid
        for i in range(9):
            if board[row][i] == n:
                return False

        # Check if encapsulating square is valid
        for i in range(3):
            for j in range(3):
                if board[(row - row%3) + i][(col - col%3) + j] == n:
                    return False 
        return True

z = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(z.solveSudoku(board))
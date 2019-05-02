class Solution(object):
    def solve(self, board):

        # Handle base case
        if len(board) == 0 or len(board[0]) == 0:
            return board

        # Get Mark all Os on the edge and their connected Os
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or j == 0 or i == len(board) -1 or j == len(board[0]) - 1:
                    self.check(board, i, j)

        # Turn unmarked Os to Xs
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        # Turn 1s (Marked Os) to original Os
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "1":
                    board[i][j] = "O"


    def check(self, board, x, y):
        # Perform a DFS of the board
        
        if board[x][y] != "O":
            return

        if board[x][y] == "O":
            board[x][y] = "1"
            if x > 0:
                self.check(board, x-1, y)
            if y > 0:
                self.check(board, x, y-1)
            if x < len(board)-1:
                self.check(board, x+1, y)       
            if y < len(board[0])-1:
                self.check(board, x, y+1)

        return

z = Solution()
matrix = [
["X","X","X","X"],
["X","O","O","X"],
["X","X","O","X"],
["X","O","X","X"]
]
print(z.solve(matrix))
print(matrix) 

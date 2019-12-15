class Solution(object):
    def update(self, board, row, col):
        living = 0
        for i in range(max(row-1, 0), min(row+2, len(board))):
            for j in range(max(col-1, 0), min(col+2, len(board[0]))):
                living += board[i][j] & 1
        if living == 3 or (living == 4 and board[row][col]):
            board[row][col]+=2

    def gameOfLife(self, board):
        for row in range(len(board)):
            for col in range(len(board[row])):
                self.update(board, row, col)
        for row in range(len(board)):
            for col in range(len(board[row])):
                board[row][col] >>= 1

a = Solution()
b = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
a.gameOfLife(b)
print(b)

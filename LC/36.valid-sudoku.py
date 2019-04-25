class Solution(object):
    def isValidSudoku(self, board):
        rows = [{} for i in range(9) ] 
        cols = [{} for i in range(9) ]
        squares = [ {} for i in range(9)]

        for i in range(9):
            for j in range(9):
                #print("iter", i, j, board[i][j])
                #print(rows)
                #print(cols)
                #print(squares)

                # Get current board value and disregard blanks
                cur_val = board[i][j]
                if cur_val == ".":
                    continue

                # Check row hashmap
                if cur_val in rows[i]:
                    return False
                rows[i][cur_val] = True

                # Check columns hashmap
                if cur_val in cols[j]:
                    return False
                cols[j][cur_val] = True

                # Check Squares hashmap
                square_col = int(i/3) + int(j/3)*3      
                if cur_val in squares[square_col]:
                    return False
                squares[square_col][cur_val] = True                

        return True

board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
z = Solution()
print(z.isValidSudoku(board))


 

import collections

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    res = self.bfs(board, i, j)
        return res

    def check_valid(self, board):
        return board[0][0] == 1 and board[0][1] == 2 and board[0][2] == 3 and board[1][0] == 4 and board[1][1] == 5 and board[1][2] == 0

    def bfs(self, board, i, j):
        queue = [(board, i, j, 0)]
        level = 0
        seen = {}
        while queue:
            cur_board, i, j, level = queue.pop(0)
            if str(cur_board) in seen:
                continue
            seen[str(cur_board)] = True
            if self.check_valid(cur_board):
                return level
            for dir in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if dir[0] >= 2 or dir[0] < 0 or dir[1] >= 3 or dir[1] < 0:
                    continue
                new_board = [list(cur_board[0]), list(cur_board[1])]
                new_board[dir[0]][dir[1]], new_board[i][j] = new_board[i][j], new_board[dir[0]][dir[1]]
                queue.append((new_board, dir[0], dir[1], level+1)) 

        return -1

z = Solution()
board = [[4, 1, 2], [5, 0, 3]]
#board = [[1, 2, 3], [4, 0, 5]]
#board = [[1, 2, 3], [5, 4, 0]]
a = z.slidingPuzzle(board)
print(a)

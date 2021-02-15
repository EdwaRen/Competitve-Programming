class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]

        DFS with backtracking in O(n!) time.
        We modify the board and place queens and backtrack when
        a solution doesn't work.

        Diagonal validity checck can work in a hacky way using
        r + c == row + col, the sum (or difference) between a queen
        and the candidate cell will be equal if they are on diagonals

        If columns and diagonal sums and diagonal differences are cached in a set,
        a position can be checked if it interferes with n other queens in
        just O(1) time. 
        """
        self.res = []
        board = [['.' for i in range(n)] for j in range(n) ]
        self.dfs(0, board, n, [set(), set(), set()])
        return self.res

    def dfs(self, row, board, n, queens):
        if n == row:
            self.res.append(["".join(r) for r in board])
            return

        for col in range(n):
            if self.is_valid(row, col, queens):
                self.update_caches(row, col, board, queens)
                self.dfs(row+1, board, n, queens)
                self.remove_caches(row, col, board, queens)

    def update_caches(self, row, col, board, queens):
        board[row][col] = 'Q'
        queens[0].add(col)
        queens[1].add(col + row)
        queens[2].add(col - row)

    def remove_caches(self, row, col, board, queens):
        queens[0].remove(col)
        queens[1].remove(col + row)
        queens[2].remove(col - row)
        board[row][col] = '.'

    def is_valid(self, row, col, queens):
        if col in queens[0] or col + row in queens[1] or col - row in queens[2]:
            return False
        return True


z = Solution()
n = 6
res = z.solveNQueens(n)
for i in res:
    print("\n\nNEW QUEEN: ")
    for j in i:
        print(j)


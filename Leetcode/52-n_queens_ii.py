class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]

        Almost a direct carbon copy of Leetcode #51

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
        self.res = 0
        self.dfs(0, n, [set(), set(), set()])
        return self.res

    def dfs(self, row, n, queens):
        if n == row:
            self.res+=1
            return

        for col in range(n):
            if self.is_valid(row, col, n, queens):
                self.update_caches(row, col, queens)
                self.dfs(row+1, n, queens)
                self.remove_caches(row, col, queens)

    def update_caches(self, row, col, queens):
        queens[0].add(col)
        queens[1].add(col + row)
        queens[2].add(col - row)

    def remove_caches(self, row, col, queens):
        queens[0].remove(col)
        queens[1].remove(col + row)
        queens[2].remove(col - row)

    def is_valid(self, row, col, n, queens):
        if col in queens[0] or col + row in queens[1] or col - row in queens[2]:
            return False
        return True


z = Solution()
n = 6
print(z.totalNQueens(n))



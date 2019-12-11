class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not len(word):
            return True
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    if self.recurse(row, col, board, word):
                        return True
        return False
    def recurse(self, i, j, board, word):
        if len(word) <= 0:
            return True
        if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
            return False
        if board[i][j] != word[0]:
            return False
        else:
            board[i][j] = "*"
            surrounds = self.recurse(i+1, j, board, word[1:]) or self.recurse(i, j+1, board, word[1:]) or \
                        self.recurse(i-1, j, board, word[1:]) or self.recurse(i, j-1, board, word[1:])
            board[i][j] = word[0]
            return surrounds

a = Solution()
board = [
    ["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"]
]
word = "aaaaaaaaaaaaa"
print(a.exist(board, word))
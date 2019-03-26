class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        # Use extra space to enable O(1) move victory detecter
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag_l = 0
        self.diag_r = 0        
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        add = 1
        
        # Fill conditions based on player
        if player == 1:
            add = 1 
        else:
            add = -1

        # Update rows and column fill
        self.rows[row]+=add
        self.cols[col]+=add

        # Update diagonal
        if row == col:
            self.diag_l += add
        if row + col == (self.n)-1:
            self.diag_r += add

        # Check for victory condition
        if abs(self.rows[row]) == self.n or \
             abs(self.cols[col]) == self.n or \
             abs(self.diag_l) == self.n or \
             abs(self.diag_r) == self.n:
            return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
obj = TicTacToe(4)
param_1 = obj.move(0,0,1)

print(param_1)

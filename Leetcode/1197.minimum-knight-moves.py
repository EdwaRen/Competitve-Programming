class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        """
        Key observations:
            Doesn't matter what quadrant we start in, hence use abs()
            Since we only care about # of moves, whenever our coordinate is
                negative, it is takes the same number of moves as its 
                reflection along the axis. Thus we can use abs()
            Our base case catches almost everything within a 3x3 square in
                quadrant I
            Instead of moving the knight, it is equivalent to just move the 
                target
            
        """

        # Cache (memoization) is absolutely necessary to prevent TLE
        self.cache = {}
        def dfs(x, y):
            if (x, y) in self.cache:
                return self.cache[(x, y)]

            # Handle base cases
            if x + y == 0:
                return 0
            elif x + y == 2:
                return 2
            elif x == 2 and y == 2:
                return 4

            # BFS recurse

            self.cache[(x, y)] = min(dfs(abs(x-1), abs(y-2)), dfs(abs(x-2), abs(y-1))) + 1
            return self.cache[(x, y)]
        return dfs(abs(x), abs(y))

z = Solution()
x = 2
y = 112
print(z.minKnightMoves(x, y))

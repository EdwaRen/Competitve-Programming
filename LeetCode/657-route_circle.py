class Solution(object):
    def judgeCircle(self, moves):
        Top = Side = 0
        for move in moves:
            if move == 'U':
                Top+=1
            elif move == 'D':
                Top-=1
            elif move == 'L':
                Side+=1
            elif move=='R':
                Side-=1
        return Top == 0 and Side == 0
a = Solution()
print(a.judgeCircle("UU"))

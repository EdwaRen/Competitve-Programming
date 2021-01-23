class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        # magnitutes represent [up, right, down, left]
        magnitudes = [0, 0, 0, 0] 

        # direction which indicates the selected magnitude's cardinality
        direction = 0

        # walk or change direction
        for i in instructions:
            if i == 'G':
                magnitudes[direction]+=1
            elif i == 'L':
                direction = (direction-1)%4
            elif i == 'R':
                direction = (direction+1)%4

        # Account for opposite direction
        ud = magnitudes[0] - magnitudes[2]
        rl = magnitudes[1] - magnitudes[3]

        return (ud == 0 and rl == 0) or direction != 0
        
z = Solution()
ins = "GRGL"
print(z.isRobotBounded(ins))
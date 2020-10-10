class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        d_walk = {'N': [0, 1], 'E': [1, 0], 'S': [0, -1], 'W': [-1, 0]}
        rotateCW = {'N': 'E', 'E': 'S', 'S': 'W', 'W':'N'}
        rotateCCW = {'N': 'W', 'E': 'N', 'S': 'E', 'W':'S'}

        # obj_hash = [(x[0], x[1]) for x in obstacles]
        obj_hash = set(map(tuple, obstacles))

        pos = [0, 0]
        point = 'N'
        max_distance = 0

        for cmd in commands:
            if cmd == -1:
                point = rotateCW[point]
            elif cmd == -2:
                point = rotateCCW[point]
            else:
                for _ in range(cmd):
                    if ((pos[0] + d_walk[point][0], pos[1] + d_walk[point][1]) in obj_hash):
                        break
                    pos[0] += d_walk[point][0]
                    pos[1] += d_walk[point][1]

            max_distance = max(max_distance, pos[0]**2 + pos[1]**2)

        return max_distance

z = Solution()
commands = [4,-1,4,-2,4]
obstacles = [[2, 4]]
print(z.robotSim(commands, obstacles))
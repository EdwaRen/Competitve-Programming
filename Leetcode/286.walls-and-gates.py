import collections

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """

        # Handle edge case
        if not rooms or len(rooms) == 0:
            return []

        # Grab all opening gates and save them to a queue
        N, M = len(rooms[0]), len(rooms)
        queue = collections.deque()
        for row in range(M):
            for col in range(N):
                if rooms[row][col] == 0:
                    queue.append((row, col, 0))

        # BFS the queue
        while queue:
            row, col, depth = queue.popleft()

            # Move in all possible directions
            for move in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if move[0] < 0 or move[0] >= M or move[1] < 0 or move[1] >= N:
                    continue 
                
                # Empty room detected
                if rooms[move[0]][move[1]] >= 2147483647:
                    queue.append((move[0], move[1], depth+1))
                    rooms[move[0]][move[1]] = depth+1

        return rooms 

z = Solution()
inf = 2147483647
grid = [
    [inf,  -1,  0,  inf],
    [inf, inf, inf,  -1],
    [inf,  -1, inf,  -1],
    [  0,  -1, inf, inf]
]
res = z.wallsAndGates(grid)
for i in res:
    for j in i:
        print(j, end=' ')
    print()
import heapq

class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        """
        Priority queue and BFS:
        Basic idea is to bfs from the largest possible tile at each iteration.
        We ensure largest seen tile is the start using a priority queue
        The tile value is the minimum of the previous bfs depth and the current value
            val = min(max_val, A[row][col])
        """
        M, N = len(A), len(A[0])
        heap = [(-A[0][0], 0, 0)]
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        max_val = 9999999
        visited = set([(0, 0)])

        # Priority queue
        while heap:
            depth, row, col = heapq.heappop(heap)
            max_val = min(max_val, -depth)
            
            # If at the final tile, return the current max value
            # Otherwise we'd continue using the bfs, while lowering max_val
            if row == M-1 and col == N -1:
                return max_val

            # All possible moves
            for move in directions:
                row_next, col_next = move[0] + row, move[1] + col
                
                # Conditions to skip
                if row_next < 0 or row_next >= M or col_next < 0 or col_next >= N or (row_next, col_next) in visited: 
                    continue 
                visited.add((row_next, col_next))

                # Update cur depth then add it back to the heap
                cur_depth = min(-depth, A[row_next][col_next])
                heapq.heappush(heap, (-cur_depth, row_next, col_next))

        return max_val        

z = Solution()
A = [
    [1,1,0,3,1,1],
    [0,1,0,1,1,0],
    [3,3,1,3,1,1],
    [0,3,2,2,0,0],
    [1,0,1,2,3,0]
]
# A = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
print(z.maximumMinimumPath(A))



        

class Solution(object):

    def __init__(self):
        # Count of islands
        self.count = 0

    def find(self, parent, loc):
        # Use path compression to increase amortized time complexity
        # Basically just finds the root
        if parent[loc] != loc:
            parent[loc] = parent[parent[loc]]
            return self.find(parent, parent[loc])
        return loc
    
    def union(self, parent, loc1, loc2):
        # Checks if the two roots are the same. Unions them together if they are not
        rootA = self.find(parent, loc1)
        rootB = self.find(parent, loc2)

        # Since we merged two distinct islands, we decrease count by one
        if parent[rootA] != rootB:
            parent[rootA] = rootB
            self.count -=1


    def numIslands(self, grid):
        # Catch edge case
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        # useful shortcuts
        N = len(grid)
        M = len(grid[0])

        # Parent stores every island's parent. Initially set as themselves
        parent = [i for i in range(N*M)]

        # Union Find
        for row in range(N):
            for col in range(M):
                
                # Union find when two adjacent ones are detected
                if grid[row][col] =="1":
                    
                    # Assume island is by itself, increase count of connected graphs (islands)
                    self.count +=1

                    # Check indexing before union find
                    if row-1 >= 0 and grid[row-1][col] == "1":
                        self.union(parent, (row*M) + col, (row-1)*M + col)
                    if row+1 < len(grid) and grid[row+1][col] == "1":
                        self.union(parent, (row*M) + col, (row+1)*M + col)
                    if col - 1 >= 0 and grid[row][col-1] == "1":
                        self.union(parent, (row*M) + col, (row*M) + col-1)
                    if col+1 < len(grid[row]) and grid[row][col+1] == "1":
                        self.union(parent, (row*M) + col, (row*M) + col+1)
        return self.count

z = Solution()
islands = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"], 
    ["0", "0", "1", "0", "0"], 
    ["0", "0", "0", "1", "1"] 
]
print(z.numIslands(islands))

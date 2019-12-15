import collections

class Solution(object):

    # Find in Union Find
    def find(self, parents, loc1):
        # Use path compression for amortized O(1)
        if parents[loc1] != loc1:
            parents[loc1] = parents[parents[loc1]]
            return self.find(parents, parents[loc1])
        return loc1

    # Union in Union Find
    def union(self, parents, loc1, loc2):
        print("union", loc1, loc2)
        rootA = self.find(parents, loc1)
        rootB = self.find(parents, loc2)

        # Combine different roots, reduce island count by one
        if rootA != rootB:
            parents[rootA] = rootB
            self.count -=1


    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        # Keep track of parents and all previously seen islands
        parents = [i for i in range(m*n)]
        seen = collections.defaultdict(bool)
        self.count = 0
        res = []

        for pos in positions:
            print(m, n, pos)
            x, y = pos[0], pos[1]

            # Skip duplicates
            if seen[(x, y)]:
                res.append(self.count)
                continue

            # Assume island is unconnected at first
            self.count +=1

            x, y = pos[0], pos[1]
            seen[(x, y)] = True

            # Check all 4 sides
            if seen[(x-1, y)] and x-1 >= 0:
                self.union(parents, (x*n)+y, ((x-1)*n)+y)
            if seen[(x, y-1)] and y-1 >= 0:
                self.union(parents, (x*n)+y, (x*n)+y-1)
            if seen[(x+1, y)] and x+1 < m:
                self.union(parents, (x*n)+y, ((x+1)*n)+y)
            if seen[(x, y+1)] and y+1 < n:
                self.union(parents, (x*n)+y, (x*n)+y+1)

            res.append(self.count)

        return res

z = Solution()
a = [[0,0],[7,1],[6,1],[3,3],[4,1]]
print(z.numIslands2(8, 4, a))

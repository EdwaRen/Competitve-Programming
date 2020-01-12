"""
# Definition for a QuadTree node.
"""

class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        return self.recurse(grid)

    def recurse(self, subgrid):
        if self.checkMono(subgrid):
            return Node(subgrid[0][0], True, None, None, None, None)
        else:
            n = len(subgrid)
            cur = Node('*', False, None, None, None, None)
            cur.topLeft = self.recurse([[i for i in row[0:n/2]] for row in subgrid[0:n/2]])
            cur.topRight = self.recurse([[i for i in row[n/2:]] for row in subgrid[0:n/2]])
            cur.bottomLeft = self.recurse([[i for i in row[0:n/2]] for row in subgrid[n/2:]])
            cur.bottomRight = self.recurse([[i for i in row[n/2:]] for row in subgrid[n/2:]])

            return cur

    # Check all squares in the grid are valid
    def checkMono(self, subgrid):
        return all([col == subgrid[0][0] for row in subgrid for col in row ])

z = Solution()
grid = [
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
]

res = z.construct(grid)
def printQuad(res):
    q = [(res, 0)]

    while q:
        cur, depth = q.pop(0)
        if not cur:
            continue

        print("cur value", cur.val)
        if not cur.isLeaf:
            q.append((cur.topLeft, depth+1))
            q.append((cur.topRight, depth + 1))
            q.append((cur.bottomLeft, depth + 1))
            q.append((cur.bottomRight, depth + 1))

printQuad(res)
    
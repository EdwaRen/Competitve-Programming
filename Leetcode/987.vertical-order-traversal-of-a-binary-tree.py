import collections 

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # Global map of levels
        level_map = collections.defaultdict(list)
        stack = [(root, 0)]

        if not root:
            return None 

        # We iterate through every vertical LAYER with this stack
        while stack:
            next_stack = []

            # Current level map to solve the issue of needing to order elements by value
            cur_map = collections.defaultdict(list)

            for i in stack:
                cur, level = i[0], i[1]
                if cur.left:
                    next_stack.append((cur.left, level-1))
                if cur.right: 
                    next_stack.append((cur.right, level+1))
                cur_map[level].append(cur.val)

            # We set the next stack to be all nodes on the next layer
            stack = next_stack

            # If 2 nodes happen to be on the same layer, then we sort them
            for level in cur_map:
                level_map[level].extend(sorted(cur_map[level]))

        # Return sorted by keys
        return [level_map[i] for i in sorted(level_map)]

z = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
a.left = b 
a.right = c  
b.left = d   
b.right = e
c.left = f 
c.right = g  
res = z.verticalTraversal(a)
print(res)
        

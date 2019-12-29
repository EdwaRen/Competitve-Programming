# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections 

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        
        # Maps index to list of values
        axis_vals = collections.defaultdict(list)
        queue = collections.deque() # Essentially just a queue
        queue.appendleft((root, 0)) # Start off queue with root

        # Keep track of the min and max depth to convert result to list
        min_axis, max_axis = 0, 0

        # In order traversal 
        while queue:
            cur, depth = queue.pop()
            axis_vals[depth].append(cur.val)

            # Only add new items to traverse if it is a valid Node
            if cur.left:
                queue.appendleft((cur.left, depth-1))
                min_axis = min(min_axis, depth-1)
            if cur.right:
                queue.appendleft((cur.right, depth+1))
                max_axis = max(max_axis, depth+1)
        
        # Convert dictionary to list of lists
        res = []
        for i in range(min_axis, max_axis+1):
            res.append(axis_vals[i])
        return res 

z = Solution()
a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(8)
d = TreeNode(4)
e = TreeNode(0)
f = TreeNode(1)
g = TreeNode(7)

a.left = b 
a.right = c  
b.left = d   
b.right = e 
c.left = f 
c.right = g 
print(z.verticalOrder(g))

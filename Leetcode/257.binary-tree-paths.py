# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections 

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # Handle edge case
        if not root:
            return []

        # Save to-traverse nodes with a queue
        queue = collections.deque()
        queue.append((root, ''))
        res = []

        while queue:
            cur, query = queue.pop()
            query += str(cur.val)

            # Append path on leaf node
            if cur.left is None and cur.right is None:
                res.append(query)
            else:

                # Add children to queue
                query += '->'
                if cur.left:
                    queue.append((cur.left, query))
                if cur.right:
                    queue.append((cur.right, query))
        return res 

z = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b 
a.right = c
b.right = e

print(z.binaryTreePaths(a))
        

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # Handle edge case
        if not root:
            return []

        # Log all border points in lists
        self.bound_left, self.bound_right = [root.val], []
        self.leafs = []

        # In order traversal
        def recurse(node, flag_left, flag_right):
            if node.left != None or node.right != None:
                # Found a left or right border. This is NOT done in inorder
                if flag_left:
                    self.bound_left.append(node.val)
                elif flag_right:
                    self.bound_right.append(node.val)

            # In order recurse
            if node.left:
                recurse(node.left, flag_left, flag_right if not node.right else False)

            # Found a leaf
            if not node.left and not node.right:
                self.leafs.append(node.val)
            if node.right: 
                recurse(node.right, flag_left if not node.left else False, flag_right)
        
        # Initialize queue
        if root.left: recurse(root.left, True, False) 
        if root.right: recurse(root.right, False, True) 
        
        return self.bound_left + self.leafs + self.bound_right[::-1]

z = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
i = TreeNode(9)
j = TreeNode(10)

a.left = b 
a.right = c
b.left = d  
b.right = e 
c.left = f 
f.left = i 
f.right = j 

e.left = g 
e.right = h
# c.left = d
# g.right = f

print(z.boundaryOfBinaryTree(a))

        

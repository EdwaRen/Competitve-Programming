# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inOrderTraverse(self, root):
        """
        Validates if a tree is a propery binary search tree (BST) with in-order traversal
        """
        if root == None:
            return true
        stack = []
        prev = None

        #Iterative in-order traversal
        while root != None or len(stack) > 0:

            # adds in everything to the left
            while root != None:
                stack.append(root)
                root = root.left

            # Only checks 1 layer above but due to properties of BST, this is the only necessary check
            root = stack.pop()
            if (prev != None and root != None and root.val <= prev.val):
                return False

            # Sets variables for the next loop round. Also shifts root to the right node.
            prev = root
            root = root.right
        return True


    def isValidBST(self, root):
        return self.inOrderTraverse(root)


a = TreeNode(4)
b = TreeNode(1)
c = TreeNode(6)
d = TreeNode(5)
e = TreeNode(11)
f = TreeNode(2)
a.left = b
a.right = c
c.left = d
c.right = e
e.left = f

s = Solution()
p = s.isValidBST(a)
print(p)

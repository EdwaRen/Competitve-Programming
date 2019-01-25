# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        # Handle edge case
        if not root:
            return 0

        # Set global max
        self.max_len = 0

        # Recurse
        self.recurse(root)

        # self.max_len returns max number of nodes, max path is just one less
        return self.max_len -1

    def recurse(self, root):
        # Handle None case
        if not root:
            return 0

        # Recurse left and right
        left = self.recurse(root.left)
        right = self.recurse(root.right)

        # Set max_len
        if left+right +1 > self.max_len:
            self.max_len = left+right+1

        # Return whichever side is bigger, +1 for current node
        root.val = max(left, right) + 1
        return root.val


# z = Solution()
# a = TreeNode(1)
# b = TreeNode(2)
# c = TreeNode(3)
# d = TreeNode(4)
# e = TreeNode(5)
# f = TreeNode(6)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# e.left = f
# print(z.diameterOfBinaryTree(a))

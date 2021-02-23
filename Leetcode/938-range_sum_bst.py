# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0

        self.res = 0
        self.dfs(root, low, high)
        return self.res

    def dfs(self, node, low, high):
        if node.val >= low and node.val <= high:
            self.res+= node.val
        if node.val >= low and node.left:
            self.dfs(node.left, low, high)
        if node.val <= high and node.right:
            self.dfs(node.right, low, high)

z = Solution()

print(z.rangeSumBST())

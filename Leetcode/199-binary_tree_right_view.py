# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        views = {}
        self.dfs(root, 0, views)
        return views.values()
        
    def dfs(self, node, depth, views):
        if not node:
            return
        views[depth] = node.val 
        self.dfs(node.left, depth+1, views)
        self.dfs(node.right, depth+1, views)
        
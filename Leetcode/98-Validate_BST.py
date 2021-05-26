# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, float('-inf'), float('inf'))
    
    def dfs(self, node, smallest, biggest):
        if node.val <= smallest or node.val >= biggest:
            return False
        
        if node.left:
            if not self.dfs(node.left, smallest, node.val):
                return False
            
        if node.right:
            if not self.dfs(node.right, node.val, biggest):
                return False
                
        return True
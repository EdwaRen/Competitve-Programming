# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        level = deque()
        level.append(root)
        res = []
        
        while level:
            n = len(level)
            level_sum = 0
            for i in range(n):
                cur = level.popleft()
                level_sum += cur.val
                if cur.right: level.append(cur.right)
                if cur.left: level.append(cur.left)
            
            res.append(level_sum / float(n))
        return res
                    
        
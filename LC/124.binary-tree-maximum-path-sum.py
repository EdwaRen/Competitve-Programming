# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.sumleft = 0
        self.sumright = 0
        node_sum = 0

class Solution(object):
    def maxPathSum(self, root):
        nodes_seen = {}

        def recurse(cur):
            # if cur in nodes_seen:
            #     return nodes_seen[cur]
            if not cur:
                return 0
            # candidate_sum = cur.val + max(cur.right.node_sum, cur.left.node_sum)
            child_max = max(cur.right.node_sum, cur.left.node_sum)
            candidate_sum = cur.val + child_max

            if candidate_sum > cur.val:
                return candidate_sum
            else:
                if cur.val < child_max:
                    return 0
                elif candidate_sum < 0:
                    return 0
                elif child_max < 0 and cur.val > 0:
                    return cur.val
                elif child_max >= 0 and cur.val >= 0:
                    return candidate_sum
                elif


        """
        :type root: TreeNode
        :rtype: int
        """
        

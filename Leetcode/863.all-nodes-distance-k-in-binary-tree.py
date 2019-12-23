# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        res = []

        def recurse(node, parent, K, target, res):
            if not node:
                return None 
            elif parent == 0:
                res.append(node.val)
                return None
            elif node.val == target:
                if K == 0:
                    res.append(node.val)
                else:
                    recurse(node.left, K-1, K, target, res)
                    recurse(node.right, K-1, K, target, res)
                return K-1
            else:
                left_rec = recurse(node.left, parent-1, K, target, res)
                right_rec = recurse(node.right, parent-1, K, target, res)
                
                if left_rec == 0 or right_rec == 0:
                    res.append(node.val)
                elif left_rec != None:
                    recurse(node.right, left_rec-1, K, target, res)
                    return left_rec-1
                elif right_rec != None:
                    recurse(node.left, right_rec-1, K, target, res)
                    return right_rec-1
                return None

        recurse(root, -1, K, target.val, res)
        return res
            
z = Solution()
a = TreeNode(3)
b = TreeNode(5)
c = TreeNode(1)
a.left = b 
a.right = c  
d = TreeNode(6)
e = TreeNode(2)
b.left = d   
b.right = e  
f = TreeNode(7)
g = TreeNode(4)
e.left = f 
e.right = g 

h = TreeNode(0)
i = TreeNode(8)
c.left = h 
c.right = i 

res = z.distanceK(a, b, 2)
print(res)

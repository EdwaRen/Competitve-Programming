# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        # Handle edge case
        if not root:
            return []    
    
        # Init stacks
        stack = [root]
        res = []
        level = 0

        # Iterate through tree
        while stack:
           
            # Create new list in res 
            res.append([])
            orig_len = len(stack)
                       
            # Iterate through the current level, with the original stack length
            for i in range(orig_len):

                # Swap adding order
                if level % 2:
                    cur = stack.pop(0)
                    if cur.right:
                        stack.append(cur.right)
                    if cur.left:
                        stack.append(cur.left)
                else:
                    cur = stack.pop()
                    if cur.left:
                        stack.insert(0, cur.left)
                    if cur.right:
                        stack.insert(0, cur.right)
                
                # Append to current list
                res[level].append(cur.val)
            
            # Trahck depth level
            level+=1            

        # Handle case where the bottom level is only None values     
        if not res[-1]:
            res.pop()

        # return
        return res

z = Solution()
a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b
a.right = c
c.left = d
c.right = e

print(z.zigzagLevelOrder(a))





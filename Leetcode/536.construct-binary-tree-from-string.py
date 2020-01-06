# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s or len(s) == 0:
            return None 

        # Hold node who's left node will be the root
        cur = TreeNode(None)
        dummy = cur

        # Keep track of depth using a stack (preorder search)
        stack = []
        i = 0
        while i < len(s):

            # Append cur node so we can remember it when attaching a right node
            if s[i] == '(':
                stack.append(cur)
            elif s[i] == ')':
                cur = stack.pop()
            else:
                # Get the value from the string
                j = i
                while i+1 < len(s) and (s[i+1] != '(' and s[i+1] != ')'):
                    i+=1

                # Attach to current node
                if not cur.left:
                    cur.left = TreeNode(s[j:i+1])
                    cur = cur.left
                elif not cur.right:
                    cur.right = TreeNode(s[j:i+1])
                    cur = cur.right
            i+=1

        return dummy.left

z = Solution()
s = "-4(-2(3)(-1))(6(-5)(7))"
res = z.str2tree(s)

def binaryPrint(cur, d):
    ret = ""
    if not cur:
        return

    if cur.right != None:
        ret += binaryPrint(cur.right, d + 4)

    ret += "\n" + (" " * d) + str(cur.val)

    if cur.left != None:
        ret += binaryPrint(cur.left, d + 4)

    return ret
print(res.val)
print(res.left, res.right)
print(binaryPrint(res, 2))



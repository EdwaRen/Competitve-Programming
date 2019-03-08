# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        # Create an index to map values to their index in the inorder array.
        index_map = {val:index for index, val in enumerate(inorder) }

        # Global variable keeping track of preorder index
        self.pre_index = 0 
        return self.recurseBuild(index_map, preorder, inorder, 0, len(inorder))


    def recurseBuild(self, index_map, preorder, inorder, start, end):
        # A branch end is detected when the starting index of an array is bigger than end index        
        if start >= end:
            return None

        # split is the index in inorder which has the same value as the current root in preorder
        split = index_map[preorder[self.pre_index]]
        self.pre_index +=1

        # Create current node
        cur = TreeNode(preorder[self.pre_index-1])
        
        # Iterate with new start and end limits based on index of next preorder
        cur.left = self.recurseBuild(index_map, preorder, inorder, start, split)
        cur.right = self.recurseBuild(index_map, preorder, inorder, split+1, end)
        
        return cur

z = Solution()
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

a = (z.buildTree(preorder, inorder))
#print(z.printTree(a))




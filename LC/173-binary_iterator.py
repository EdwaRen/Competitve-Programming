# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self.ts = []
        cur = root
        self.pushLeft(cur)

    def hasNext(self):
        return self.ts

    def next(self):
        temp = self.ts.pop()
        a = temp.val
        if temp.right != None:
            temp = temp.right
            self.pushLeft(temp)
        return a

    def pushLeft(self, root):
        cur = root
        while cur != None:
            self.ts.append(cur)
            cur = cur.left

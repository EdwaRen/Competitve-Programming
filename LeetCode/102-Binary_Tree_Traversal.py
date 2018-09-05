import Queue

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def levelOrder(self, node):
        if node == None:
            return []
        q = Queue.Queue()
        q.put(node)
        res = [[node.val]]
        while q.empty() == False:
            cur_level = q.qsize()
            level_list = []
            for i in range(cur_level):
                cur = q.get()
                if cur.left != None:
                    q.put(cur.left)
                    level_list.append(cur.left.val)
                if cur.right != None:
                    q.put(cur.right)
                    level_list.append(cur.right.val)
            if level_list != []:
                res.append(level_list)
        return res

s = Solution()
a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
f = TreeNode(2)
g = TreeNode(1)
a.left = b
# b.left = TreeNode(4)
a.right = c
c.left = d
c.right = e
# e.right = f
# f.left = g

print(s.levelOrder(a))

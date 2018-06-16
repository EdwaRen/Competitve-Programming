class Solution:

    class node:
        def __init__(self, count, children, parent):
            self.count = count
            self.children = children
            self.parent = parent
        def add_child(self, child):
            self.children.append(child)


    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from collections import deque

class NestedIterator(object):

    def __init__(self, nestedList):
        self.list_q = deque([])
        for i in nestedList:
            if i.isInteger():
                self.list_q.appendleft(i.getInteger())
            else:
                new_list = NestedIterator(i.getList())
                while new_list.hasNext():
                    self.list_q.appendleft(new_list.next())

    def next(self):
        return self.list_q.pop()

    def hasNext(self):
        if self.list_q:
            return True
        else:
            return False


# Your NestedIterator object will be instantiated and called as such:
b = [[1,1],2,[1,3]]
i, v = NestedIterator(b), []
while i.hasNext(): v.append(i.next())
print(v)

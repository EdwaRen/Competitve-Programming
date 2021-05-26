class Node:
    def __init__(self, start, end):
        self.start = start 
        self.end = end
        self.left = None
        self.right = None
    
    def insert(self, cur, start, end):
        if cur.start >= end:
            if cur.left:
                return self.insert(cur.left, start, end)
            else:
                cur.left = Node(start, end)
                return True 

        elif cur.end <= start:
            if cur.right:
                return self.insert(cur.right, start, end)
            else:
                cur.right = Node(start, end)
                return True

        return False


class MyCalendar(object):

    def __init__(self):
        self.root = None
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        BST based solution approach. The BST written is very basic and unbalanced.
        If this was a Java solution then Treemap would be used as its a balanced 
        implementation.
        """
        if not self.root:
            self.root = Node(start, end)
            return True

        return self.root.insert(self.root, start, end)
        

# Your MyCalendar object will be instantiated and called as such:
z = MyCalendar()
print(z.book(10, 20))
print(z.book(15, 25))
print(z.book(20, 30))
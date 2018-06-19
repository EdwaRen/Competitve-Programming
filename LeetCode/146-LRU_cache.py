class Node:
    def __init__(self, v, k):
        self.val = v
        self.key = k
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.my_dict = {}
        self.first = Node(0, 0)
        self.last = Node(0, 0)
        self.first.prev = self.last

        self.last.next = self.first

    def get(self, key):
        if key in self.my_dict:
            self._remove(self.my_dict[key])
            self._add(self.my_dict[key])
            return self.my_dict[key].val
        else:
            return -1

    def _remove(self, node):
        a = node.prev
        b = node.next
        a.next  = b
        b.prev = a

    def _add(self, node):
        a = self.first.prev
        a.next = node
        node.prev = a
        node.next = self.first
        self.first.prev = node

    def print_list(self):
        a = self.first
        print("printing list")
        while a != None:
            print("node", a.key, a.val)
            a = a.prev

    def put(self, key, value):
        if key in self.my_dict:
            self._remove(self.my_dict[key])

        a = Node(value, key)
        self._add(a)
        self.my_dict[key] = a
        if len(self.my_dict) > self.capacity:
            del self.my_dict[self.last.next.key]
            self._remove(self.last.next)
        print("dict after put", self.my_dict)
        print("nodes after print", self.print_list())


# Your LRUCache object will be instantiated and called as such:
cache = LRUCache( 2  );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       # returns 1
cache.put(3, 3);    # evicts key 2
cache.get(2);       # returns -1 (not found)
cache.put(4, 4);    # evicts key 1
cache.get(1);       # returns -1 (not found)
cache.get(3);       # returns 3
cache.get(4);       # returns 4

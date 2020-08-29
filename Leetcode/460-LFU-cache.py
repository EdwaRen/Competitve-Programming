import collections 
import pdb

class LLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None 
        self.prev = None 

class DoubleLL:
    def __init__(self):
        """
        A custom class for doubly linked lists.
        We define our custom sentinel to make pushing and popping empty 
        linked lists easier
        """
        self.sentinel = LLNode(None, None)
        self.sentinel.next = self.sentinel.prev = self.sentinel 
        self.cur_size = 0

    def push_front(self, incoming):
        incoming.next = self.sentinel.next
        self.sentinel.next.prev = incoming 
        incoming.prev = self.sentinel
        self.sentinel.next = incoming
        self.cur_size+=1

    def pop(self, node = None):
        if self.cur_size == 0:
            return 

        if not node:
            node = self.sentinel.prev

        node.next.prev = node.prev
        node.prev.next = node.next
        self.cur_size-=1
        return node
    
    def __len__(self):
        return self.cur_size

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        Each frequency has a custom linked list 
        We track the minimum frequency with hashmaps. This frequency can always
        be found whenever we override it, usually by resetting it to one.
        """
        self.capacity = capacity
        self.cur_size = 0
        self.freq_stack = collections.defaultdict(DoubleLL)
        self.key_node_map = {}
        self.key_freq_map = {}
        self.min_freq = 1


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not self.capacity:
            return -1

        if key in self.key_freq_map:
            freq = self.key_freq_map[key]
            incoming = self.key_node_map[key]

            # Pop the existing node
            self.freq_stack[freq].pop(incoming)
            if freq == self.min_freq and not self.freq_stack[freq]:
                self.min_freq+=1

            # Push the node again with the correct frequency
            freq += 1
            self.key_freq_map[key] = freq
            self.freq_stack[freq].push_front(incoming)
            return incoming.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if not self.capacity:
            return -1
        
        if key in self.key_freq_map:
            # Pop and push again the existing node. Update value
            freq = self.key_freq_map[key]
            incoming = self.key_node_map[key]
            incoming.value = value
            self.freq_stack[freq].pop(incoming)
            if freq == self.min_freq and not self.freq_stack[freq]:
                self.min_freq+=1
            freq += 1
            self.key_freq_map[key] = freq
            self.freq_stack[freq].push_front(incoming)
        else:
            # Create a new node, update min frequency
            incoming = LLNode(key, value)
            self.key_freq_map[key] = 1
            self.key_node_map[key] = incoming

            if self.capacity == self.cur_size:
                rm = self.freq_stack[self.min_freq].pop()

                del self.key_freq_map[rm.key]
                del self.key_node_map[rm.key]
                del rm
                if not self.freq_stack[self.min_freq]:
                    del self.freq_stack[self.min_freq]
                self.cur_size-=1
            self.cur_size+=1
            self.min_freq = 1
            if not self.freq_stack[self.min_freq]:
                self.freq_stack[self.min_freq] = DoubleLL()
            self.freq_stack[self.min_freq].push_front(incoming)
            



# ["LFUCache","put","put","get","get","put","get","get","get"]
# [[2],[2,1],[3,2],[3],[2],[4,3],[2],[3],[4]]
# Your LFUCache object will be instantiated and called as such:
cache = LFUCache(2)

cache.put(2, 1)
cache.put(3, 2)
print(cache.get(3))
print(cache.get(2))
cache.put(4, 3)
print(cache.get(2))
# print(cache.get(3))
# print(cache.get(4))

# cache.put(2, 1)
# cache.put(2, 2)
# cache.put(4, 4)
# print(cache.get(0))  

# cache.put(2, 3)
# print(cache.get(2))  
# print(cache.get(1))       # returns 1
# cache.put(3, 3)    # evicts key 2
# print(cache.get(2))       # returns -1 (not found)
# print(cache.get(3))       # returns 3.
# cache.put(4, 4)    # evicts key 1.
# print(cache.get(1))       # returns -1 (not found)
# print(cache.get(3))       # returns 3
# print(cache.get(4))       # returns 4
import collections
from bisect import bisect_right

class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_store = collections.defaultdict(list)
        self.value_store = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """

        self.key_store[key].append(timestamp)
        self.value_store[key].append(value)
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        key_list = self.key_store[key]
        index =  bisect_right(key_list, timestamp)
        return self.value_store[key][index-1] if index else ''
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
obj = TimeMap()
obj.set("foo", "bar", 1)
print(obj.get("foo", 1))
print(obj.get("foo", 3))
obj.set("foo", "bar2", 5)
print(obj.get("foo", 4))
print(obj.get("foo", 5))


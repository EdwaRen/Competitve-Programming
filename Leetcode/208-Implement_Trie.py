class Node:

    def __init__(self):
        self.next = [None] * 26
        self.end = False

    def containsVal(self, val):
        return self.next[val] != None


class Trie:

    def __init__(self, value=""):
        self.root = Node()
        self.insert (value)

    def insert(self, word):
        cur = self.root
        for i in word:
            l = ord(i)-97
            if not cur.containsVal(l):
                cur.next[l] = Node()
            cur = cur.next[l]
        cur.end = True

    def search(self, word):
        cur = self.root
        for i in word:
            l = ord(i)-97
            if not cur.containsVal(l):
                return False
            cur = cur.next[l]
        return cur.end == True and cur != None


    def startsWith(self, word):
        cur = self.root
        for i in word:
            l = ord(i)-97
            if not cur.containsVal(l):
                return False
            cur = cur.next[l]
        return cur != None

pre = 'aaaaaaa'
a = Trie()
b = 'aaa'
c = 'aaaz'
(a.insert(pre))
(a.insert(b))
print(a.search(c))


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

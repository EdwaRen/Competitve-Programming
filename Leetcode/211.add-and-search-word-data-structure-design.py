import collections 

class TrieNode():
    def __init__(self, next=None):
        self.is_word = False
        self.next = collections.defaultdict(TrieNode)
        
    def addWord(self, word):
        # Recursively add word using defaultdict(TrieNode)
        cur = self
        for chr in word:
            cur = cur.next[chr]
            
        # Mark this node as a complete word
        cur.is_word = True
            
    def findWord(self, word):
        cur = self
        for i in range(len(word)):
            
            # character exists, match
            if word[i] in cur.next:
                cur = cur.next[word[i]]
                
            # If there's a dot, try all possible child nodes with DFS + backtracking
            elif word[i] == '.':
                for node in cur.next.values():
                    if node.findWord(word[i+1:]):
                        return True
                return False
            
            else:
                return False
            
        # Check that the word is complete
        return cur.is_word
        
        
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.root.addWord(word)
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.root.findWord(word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
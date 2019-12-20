import collections 

class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        cur = self.root

        # Leverages get_or_create of defaultdict to easily make our Trie
        for letter in word:
            cur = cur.children[letter]
        cur.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        # DFS through the Trie
        def dfs(index, word, node):
            if index >= len(word):
                # print("END", node.__dict__)
                return node.isWord

            if word[index] == '.':
                # Recurse through all of the current node's children if period found
                res = False
                for key, value in node.children.items():
                    res = res or dfs(index+1, word, value)
                return res
            else:
                if word[index] not in node.children:
                    return False
                return dfs(index+1, word, node.children[word[index]])

        return dfs(0, word, self.root)

# Your WordDictionary object will be instantiated and called as such:
z = WordDictionary()
z.addWord('a')
# z.root
z.addWord('ab')
# z.addWord('mad')

# res1 = z.search('pad')
# res2 = z.search('bad')
# res3 = z.search('.ad')
res4 = z.search('ab')
# print(res1)
# print(res2)
# print(res3)
print(res4)

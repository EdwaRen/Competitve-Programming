
# Normal TrieNode Implementation with addition of words field
class TrieNode:
    def __init__(self, letter=''):
        self.letter = letter 
        self.children = {}
        self.words = []

# Normal Trie Implementation but we append and sort the words at the end
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for letter in word:
           
            if letter not in cur.children:
                cur.children[letter] = TrieNode(letter)
            cur = cur.children[letter]

            # Append word
            cur.words.append(word)
            cur.words = sorted(cur.words)[:min(3, len(cur.words))]


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """

        # Add items to the Trie
        T = Trie()
        for item in products:
            T.insert(item)
        
        res = []
        cur = T.root

        # Search Trie, add words saved at each node
        continuous = True
        for letter in searchWord:
            if letter in cur.children and continuous == True:
                cur = cur.children[letter]
                res.append(cur.words)
            else:
                continuous = False
                res.append([])
        return res
            
z = Solution()
products = ["havana"]
searchWord = 'tatiana'
print(z.suggestedProducts(products, searchWord))
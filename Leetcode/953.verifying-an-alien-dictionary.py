class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_map = {}
        for index, val in enumerate(order):
            order_map[val] = index

        for i in range(len(words)-1):

            letter = 0
            while letter + 1 < min(len(words[i]), len(words[i+1])) and words[i][letter] == words[i+1][letter]:
                letter += 1

            # Check if tie breaking letter breaks order
            if order_map[words[i][letter]] > order_map[words[i+1][letter]]:
                return False
            # If it's all tied, BUT first element is longer then it is still a fail
            elif order_map[words[i][letter]] == order_map[words[i+1][letter]] and len(words[i]) > len(words[i+1]):
                return False

        return True

        


z = Solution()
words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(z.isAlienSorted(words, order))
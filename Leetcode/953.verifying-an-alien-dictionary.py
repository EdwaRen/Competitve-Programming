class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Alien dictionary that maps the order
        # Go through every two words and check if any pairing fails
        char_order = {}
        for idx, val in enumerate(order):
            char_order[val] = idx
            
        for i in range(1, len(words)):
            for j in range(len(words[i-1])):
                if j >= len(words[i]):
                    return False
                elif char_order[words[i-1][j]] > char_order[words[i][j]]:
                    return False
                elif char_order[words[i-1][j]] < char_order[words[i][j]]:
                    break

        return True
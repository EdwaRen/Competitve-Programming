from collections import Counter

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        Use a hash to process BALLOON and the text. Iterate through BALLOON so no characters are missed
        """
        if len(text) < 0: return 0

        mapping = Counter(text)
        balloon_chars = {'b': 1, 'a': 1, 'l': 2, 'o':2, 'n':1 }
        min_balloons = float('inf')
        
        for key, value in balloon_chars.items():
            if key in mapping:
                min_balloons = min(min_balloons, int(mapping[key] / value))
            else:
                return 0

        return min_balloons

z = Solution()
text = "lloo"
print(z.maxNumberOfBalloons(text))
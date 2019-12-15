

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """

        # Separate into digits and letter words
        digits = []
        words = []
        for l in logs:
            if l.split()[1].isnumeric():
                digits.append(l)
            else:
                words.append(l)
        
        # Sort first by identifier, then by content
        words = sorted(words, key = lambda x: x.split()[0])
        words = sorted(words, key = lambda x: x.split()[1:])
        return words + digits


z = Solution()
logs = ["t kvr", "r 3 1", "i 403", "7 so", "t 54"]
print(z.reorderLogFiles(logs))
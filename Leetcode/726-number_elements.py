import collections

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str

        Traverse backwards and keep track of many things :')
        """
        mult_stack = []
        mappings = collections.defaultdict(int)
        element = ''
        freq = ''
        multiplier = 1

        i = len(formula)-1
        while i >= 0:
            if formula[i].isdigit():
                freq += formula[i]
            elif formula[i].islower():
                element += formula[i]
            elif formula[i].isupper():                
                element += formula[i]
                local_freq = 1 if freq == '' else int(freq[::-1])
                mappings[element[::-1]] += multiplier * local_freq
                element = ""
                freq = ''
            elif formula[i] == ')':
                if freq == '':
                    freq = '1'
                freq = int(freq[::-1])
                mult_stack.append(freq)
                multiplier *= freq
                freq = ''
            elif formula[i] == '(':
                multiplier /= mult_stack.pop()
            i-=1

        res = ""
        for key in sorted(mappings.items(), key=lambda item: item[0]):
            res += str(key[0])
            if key[1] > 1: res += str(key[1])
        return res

z = Solution()
formula = "K4(ON(SO3)2)2"
# formula = "H50"
# {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
formula = '(H)'
print(z.countOfAtoms(formula))

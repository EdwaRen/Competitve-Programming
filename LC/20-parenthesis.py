class Solution:
    def isValid(self, s):
        o = ['{', '(', '[']
        c = ['}', ')', ']']
        occurances = {}
        occurances['{'] = '}'
        occurances['('] = ')'
        occurances['['] = ']'
        list_occ = []
        for letter in s:
            if letter in o:
                list_occ.append(letter)
            elif letter in c:
                if len(list_occ) ==0 :
                    return False
                if letter == occurances[list_occ[len(list_occ)-1]]:
                    del list_occ[-1]
                else:
                    return False
        if len(list_occ):
            return False
        return True
a = Solution()
print(a.isValid("[]"))

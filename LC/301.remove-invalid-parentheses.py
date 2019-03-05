class Solution(object):
    def __init__(self):
        self.ans = {}

    def removeInvalidParentheses(self, s):
        # Find left_extra and right_extra
        left_ext = 0
        right_ext = 0
        for i in s:
            if i == '(':
                left_ext += 1
            elif i == ')':
                if left_ext <= 0:
                    right_ext+=1
                else:
                    left_ext -=1
        self.recurse(s, 0, 0, 0, left_ext, right_ext, '')
        return list(self.ans.keys())

    def recurse(self, s, index, left_count, right_count, left_ext, right_ext, cur):
        if index == len(s):
            if left_ext == 0 and right_ext == 0:
                self.ans[cur] = 1
        else:
            if s[index] == '(' and left_ext > 0:
                self.recurse(s, index+1, left_count, right_count, left_ext -1, right_ext, cur)   
            if s[index] == ')' and right_ext > 0:
                self.recurse(s, index+1, left_count, right_count, left_ext, right_ext-1, cur)
            if s[index] != ')' and s[index] != '(':
                self.recurse(s, index+1, left_count, right_count, left_ext, right_ext, cur + s[index])
            elif s[index] == ')' and right_count < left_count:
                self.recurse(s, index+1, left_count, right_count +1, left_ext, right_ext, cur + ')')
            elif s[index] == '(':
                self.recurse(s, index+1, left_count +1, right_count, left_ext, right_ext, cur + '(')
        
z = Solution()
s = "(a)())()"
print(z.removeInvalidParentheses(s))

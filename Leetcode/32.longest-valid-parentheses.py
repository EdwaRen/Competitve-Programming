class Solution(object):
    def longestValidParentheses(self, s):
        # Set init variables
        left = 0
        right = 0
        valid_start = 0
        res = 0
        
        # Check with the starting longest valid bracket being a left close bracket
        for i in range(len(s)):

            if s[i] == '(':
                left +=1

            elif s[i] == ')':
                right +=1        

                # Valid parenthesis detected
                if left == right:
                    res = max(res, i - valid_start + 1)                  

                # Reset counters if there are more right brackets, everything before is no longer considered       
                elif right > left:
                    valid_start = i +1
                    left = 0
                    right = 0

        # Reset Variables
        left = 0
        right = 0
        valid_start = len(s) -1 
        
        # Check with the starting longest bracket being a right close one
        for i in range(len(s)):
            r_i = len(s) - i -1 
        
            if s[r_i] == '(':
                left +=1
        
                # Valid parenthesis detected
                if left == right:
                    res = max(res, valid_start-r_i+1)

                # Reset counters if there are more left brackets. Everything after is no longer considered
                elif left > right:
                    valid_start = r_i-1
                    left = 0
                    right = 0

            elif s[r_i] == ')':    
                right +=1
        
        return res

z = Solution()
s = "()((())"

print(z.longestValidParentheses(s))











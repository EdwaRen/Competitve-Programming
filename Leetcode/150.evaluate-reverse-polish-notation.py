class Solution(object):
    def evalRPN(self, tokens):
        
        # Use stack to track each new number
        stack = []

        # Iterate through tokens
        for i in tokens:    

            # Check if operator detected
            if i in ["+", "-", "/", "*"]:
                
                # Pop off the last two elements of the stack
                prev1 = int(stack.pop())
                prev2 = int(stack.pop())
            
                # Perform the necessary operations with the last two. Then append the result to the end of the stack
                if i == "+":
                    stack.append(prev2 + prev1)
                elif i == "-":
                    stack.append(prev2 - prev1)
                elif i == "*":
                    stack.append(prev2 * prev1)
                elif i == "/":
                    stack.append( int(prev2/prev1) )

            else:
                # If the token is a number, append it
                stack.append(i)

        # Stack should be a single element now
        return int(stack.pop())

z = Solution()
#tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
tokens = ["4", "3", "-"]
print(z.evalRPN(tokens))




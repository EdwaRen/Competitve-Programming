class Solution(object):
    def calculate(self, s):
        # Keep track of previous operation
        prev = '+'

        # Keep track of current number
        cur_num = 0

        # Keep track of previous numbers in poppable stack
        stack = []

        # Iterate through, with one extra step to push the last number
        for i in s + '+':
            # Update the number
            if i.isnumeric():       
                cur_num *=10
                cur_num += int(i)
                continue

            # skip spaces
            elif i == ' ':
                continue

            # Only executed if current number is an operation
            # However the stack update is by the previous operation
            if prev == '+':
                stack.append(cur_num)
            elif prev == '-':
                stack.append(-cur_num)
            elif prev == '*':
                stack.append( stack.pop()*cur_num)
            elif prev == '/':
                stack.append(int(stack.pop()/cur_num))
            
            # Update prev operation
            if i in ['+', '-', '*', '/']:
                prev = i
            
            # Current number reset to 0
            cur_num = 0
        
        # Add up the operation/subtraction leftovers after multiplication
        res = 0
        while stack:
            res+=stack.pop()
        
        # Return
        return res

z = Solution()
eqn = "14-3/2"
print(z.calculate(eqn))




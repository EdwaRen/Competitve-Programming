class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """

        stack = []
        for ch in expression:
            if ch == ')':
                seen = []
                while stack[-1] != '(':
                    seen.append(stack.pop())
                stack.pop()
                op = stack.pop()
                if op == '&':
                    stack.append(all(seen))
                elif op == '|':
                    stack.append(any(seen))
                elif op == '!':
                    stack.append(not seen[0])
                
            elif ch != ',':
                if ch == 't':
                    stack.append(True)
                elif ch == 'f':
                    stack.append(False)
                else:
                    stack.append(ch)

        return stack.pop()

z = Solution()
expr = "|(&(t,f,t),!(t))"
print(z.parseBoolExpr(expr))

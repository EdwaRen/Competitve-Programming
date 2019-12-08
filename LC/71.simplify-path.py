class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return ''
        
        # Keep track of directories with stack
        stack = []

        # split by slash
        path_elements = path.split('/')
        for i in path_elements:
            if i == '' or i == '.':
                continue 
            if i == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(i)

        res = '/' + '/'.join(stack)
        return res 

z = Solution()
path = "/home/"
res = z.simplifyPath(path)
print(res)
# print([].pop())

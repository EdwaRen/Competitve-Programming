class Solution(object):
    def isPalindrome(self, s):
        # Handle edge case
        if not s:
            return True

        # Initialize the two pointers
        left = 0
        right = len(s) -1
        
        # check every element single pass
        while left <= right:
                
            # Skipping non alphabetical entries
            while not s[left].isalnum() and left + 1 < len(s):
                left+=1

            while not s[right].isalnum() and right > 0:
                right -=1
                    
            # Check if left == right disregarding case
            if (s[left].lower() != s[right].lower()) and (s[left].isalnum() and s[right].isalnum()): 
                return False

            left +=1
            right -=1

        return True

z = Solution()
arr = "A man, a plan, a canal: Panama"
#arr = ".."
print(z.isPalindrome(arr))









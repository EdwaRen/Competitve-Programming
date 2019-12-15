class Solution(object):
    def numDecodings(self, s):
        
        # Keep track of previous entries rather than dp
        prev = 1
        prev_second = 1

        # handle edge case
        if s[0] == '0' and len(s) == 1:
            return 0

        # Iterate, recording and updating prev and prev_second
        for i in reversed(range(len(s))):

            # Set to 0 possibilities if the current is 0, will salvage if applicable later on
            cur = 0
            if s[i] != '0':
                cur = prev
            
            # Add second previous element if it forms a valid two digit number.            
            if i+1 < len(s)  and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
                cur += prev_second

            # Update previous variables
            prev_second = prev
            prev = cur

        # Return
        return prev





 

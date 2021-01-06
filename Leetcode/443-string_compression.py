class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        # Handle edge case
        if len(chars) == 0:
            return 0

        # Two pointers to current_char_index and next_char_index and a current character count
        cc_index = 0
        nc_index = 1
        cc_count = 1

        # Go through all chars while modifying list in place
        while cc_index < len(chars) and nc_index < len(chars):

            # New character detected, print current count to chars list while updating pointers
            if chars[cc_index] != chars[nc_index]:
                if cc_count > 1:
                    for dig in str(cc_count)[::-1]:
                        chars.insert(cc_index+1, dig)
                        nc_index+=1
                cc_index = nc_index
                cc_count=1

                # Ensure index doesn't match exactly with cc_index
                nc_index+=1

            # Pop a character as long as the indexs don't match
            elif cc_index != nc_index:
                chars.pop(nc_index)
                cc_count+=1
        
        # Update the last count
        if cc_count > 1:
            for dig in str(cc_count)[::-1]:
                chars.insert(cc_index+1, dig)
        
        return len(chars)

z = Solution()
chars = ["a","a","b","b","c","c","c"]
chars = ["a"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars = ["a","a","a","b","b","a","a"]
print(z.compress(chars))
print(chars)
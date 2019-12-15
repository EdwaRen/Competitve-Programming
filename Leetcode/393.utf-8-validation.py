class Solution(object):
    def validUtf8(self, data):
        # Masks to check last and second last bits
        mask_outer = 1 << 7
        mask_inner = 1 << 6

        # Count number of bytes the current number carries
        code_bytes = 0

        # Iterate, keeping track of number of bytes should be data-filled
        for i in data:
            
            # Find next number of bytes
            if code_bytes == 0:

                # Mask_temp will track the number of 1 bits in a row
                mask_temp = mask_outer

                # Determine number of leading 1s in the current number
                while i & mask_temp:
                    code_bytes +=1
                    mask_temp = mask_temp >> 1    
            
                # 0 bytes, next
                if code_bytes == 0:
                    continue            

                # There does not exist 5 byte number or 1 byte numbers
                if code_bytes > 4 or code_bytes == 1:
                    return False
            
            # Continuation of bits from last number, ensures first two digits are 1 and 0
            else:
                if not i & mask_outer or i & mask_inner:
                    return False
            
            code_bytes -=1
        
        # Return
        if code_bytes != 0:
            return False
        return True

z = Solution()
data = [235, 140, 4]
print(z.validUtf8(data))



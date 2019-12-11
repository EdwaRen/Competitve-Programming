class Solution(object):
    def numberToWords(self, num):
        under_twenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        under_hundred_above_twenty = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety", "Hundred"]
        thousands = ["" , "Thousand", "Million", "Billion"]
        
        def printer(remainder):
            res_print = ""

            # Handle zero case
            if remainder == 0:
                return " "

            # Get the hundreds digit
            if remainder >= 100:
                res_print += str( under_twenty[int(remainder/100)]) + " Hundred "
                        
            # Get tens and ones digit, accounting for zero
            tens = remainder%100
            
            # Under 20 is a special case due to english diction
            if tens < 20:
                res_print += under_twenty[tens] + " "
            elif tens < 100:
                res_print += under_hundred_above_twenty[ int(tens/10) - 2 ] + " "
                res_print += under_twenty[tens%10] + " "

            return res_print

        # Handle edge case
        if num == 0:
            return "Zero"

        # We subdivide the number into every thousands
        res = ""
        thousand_count = 0

        # 123000 has the same start as 123, thus we keep dividing by 1000
        while float(num / 1000.0) > 0.00001:
            # Use a helper function to determine the suffix, and add it to the beginning
            suffix = printer(num%1000)
            if suffix != " ":
                res = printer(num % 1000)  + thousands[thousand_count] + " "  + res
    
            # Update the thousand_count
            thousand_count +=1

            # Update num and round it
            num  = int(num/1000)
        res = res.split()
        res = " ".join(res)
        return res.strip()


z = Solution()
num = 1000001000
print(z.numberToWords(num))







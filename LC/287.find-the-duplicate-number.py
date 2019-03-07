class Solution(object):
    def findDuplicate(self, nums):
        crawl = nums[0]
        run = nums[0]
        init = True
        while crawl != run or init:
            init = False
            crawl = nums[crawl]
            run = nums[nums[run]]

#            print("crawl, run", crawl, run)

        crawl = nums[0]
        while crawl != run:
            run = nums[run]
            crawl = nums[crawl]       

        return crawl

z = Solution()
arr = [3, 1, 3, 4, 2]
print(z.findDuplicate(arr))



 

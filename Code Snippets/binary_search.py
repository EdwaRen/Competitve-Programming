def binary_search(nums, target):
    lo = 0
    hi = len(nums)-1

    while lo <= hi:
        # This mid func is VERY important because it shows you know about int overflows
        mid = lo + ((hi - lo) // 2)

        if target < nums[mid]:
            hi = mid - 1
        elif target > nums[mid]:
            lo = mid + 1
        elif target == nums[mid]:
            return True
    return False

nums = [1, 2, 4, 6, 7, 8, 9]
print("Finds 4, expected True")
print(binary_search(nums, 4))
print("Finds 5, expected False")
print(binary_search(nums, 5))
print("Finds 9, expected True")
print(binary_search(nums, 9))
print("Finds 0, expected False")
print(binary_search(nums, 0))

# Alternative implementation with custom conditions
# Plagiarized from here: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/discuss/777019/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.
def smallestDivisor(nums, threshold):
    def condition(divisor):
        return sum((num - 1) // divisor + 1 for num in nums) <= threshold

    left, right = 1, max(nums)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left

print("\n\nAlternative binary search to find a condition instead of \
finding a number:")

nums = [44,22,33,11,1]
T = 5
print(smallestDivisor(nums, T))

nums = [21212,10101,12121]
T = 1000000
print(smallestDivisor(nums, T))

nums = [2,3,5,7,11]
T = 11
print(smallestDivisor(nums, T))
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
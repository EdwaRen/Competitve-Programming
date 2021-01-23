import random

def partition(data, pivot):
    less, equal, greater = [], [], []
    for item in data:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            greater.append(item)
        else:
            equal.append(item)
    return less, equal, greater


def quickselect(nums, index):
    pivot = nums[random.randint(0, len(nums) - 1)]
    count = 0
    smaller, equal, larger = partition(nums, pivot)
    count = len(equal)
    mid = len(smaller)

    if mid <= index and index < mid + count:
        return pivot
    elif mid > index:
        return quickselect(smaller, index)
    else:
        return quickselect(larger, index - (mid + count))

# Quickselect to find kth number
nums = [1, 2, 5, 6, 8, 9]
third_number = quickselect(nums, 2)
print("third number is ", third_number, " of ", nums)

nums2 = [9, 9, 8, 7, 6, 9, 1]
fourth_number = quickselect(nums2, 3)
print("fourth number is ", fourth_number, " of ", nums2, sorted(nums2))

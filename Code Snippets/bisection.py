import bisect

keys = [1, 2, 3, 3, 3, 5]
print("keys = ", keys)

idx_right = bisect.bisect(keys, 3)
print("bisect right for key = 3: ", idx_right)

idx_left = bisect.bisect_left(keys, 3)
print("bisect left for key = 3: ", idx_left)


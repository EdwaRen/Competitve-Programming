import collections

# Counter In Python
# Construct -> O(n)
# Operations -> O(1)
# Note: Dict can replaces many uses of counter, like collections.defaultdict(int)

# Counts number of unique characters
dict_t = collections.Counter("aaabc")
print(dict_t)
print(dict_t['d'])
required = len(dict_t)
print(required)

z = [1, 1, 2, 3, 4, 4, 5]
print(collections.Counter(z))
print(1 in z)
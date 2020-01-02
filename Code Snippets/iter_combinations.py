import itertools

words = ["cart","home","home","cart","home"]

# No repeated elements
for i in itertools.combinations(words, 2):
    print(i, end='')

# Permutations is different because it maps elements backwards as well Ie
# cart -> home AND home -> cart

# for i in itertools.combinations(words, 2):
#     print(i, end='')


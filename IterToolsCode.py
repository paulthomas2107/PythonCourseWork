# Handle iterators
from itertools import product, permutations, combinations, accumulate, groupby, count, cycle, repeat

import operator

# Product
a = [1, 2]
b = [3, 4]
prod = product(a, b, repeat=2)  # produce cartesian product
print(list(prod))

# Permutations
a = [1, 2, 3]
perm = permutations(a, 2)  # reduce number of perms to 2 of the 3
print(list(perm))

# Combinations
a = [1, 2, 3, 4]
combo = combinations(a, 3)
print(list(combo))

# Accumulate
a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul)  # with multiply
print(list(acc))
a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(list(acc))


# Group by


def smaller_than_three(x):
    return x < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_three)
for key, value in group_obj:
    print(key, list(value))

# Lambda version
a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))

persons = [{'name': 'Paul', 'age': 26}, {'name': 'Dan', 'age': 26}, {'name': 'Lisa', 'age': 33},
           {'name': 'Clare', 'age': 55}]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

# Infinite iterators
for i in count(10): # counts for ever from 10
    print(i)
    if i == 50:
        break

# Cycle for ever
a = [1, 2, 3]
for i in cycle(a):
    print(i)

# Repeat  for ever
a = [1, 2, 3]
for i in repeat(1, 10):
    print(i)










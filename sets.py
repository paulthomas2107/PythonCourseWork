#  No dupes, immutable, unordered
mySet = {1, 1, 1, 1}

# Duplicates removed
print(mySet)
mySet = {1, 2, 2, 1}
print(mySet)
mySet = set([12, 34, 233])
print(mySet)
mySet = set("Paul Thomas")
print(mySet)

# create an empty set
mySet = set()
mySet.add('a')
mySet.add(1)
mySet.add(999)
print(mySet)
mySet.remove(1)
mySet.remove('a')
print(mySet)

# discard - search and destroy but ok if cant find
mySet = {1, 2, 3, 5}
mySet.discard(2)
mySet.discard('Do not exist')
print(mySet)
mySet.clear()
print(mySet)

mySet = {1, 2, 3, 5}
item = mySet.pop()
print(mySet)
print(item)

mySet = {1, 2, 3, 5}
for i in mySet:
    print(i)

if 2 in mySet:
    print("yes 2 is there")

# Union and intersection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

# intersection finds duplicates in sets
i = odds.intersection(evens)
print(i)
i = odds.intersection(primes)
print(i)

# Just diffs in two sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
diff = setA.difference(setB)
print(diff)
diff = setA.symmetric_difference(setB)
print(diff)
setA.update(setB)
print(setA)
# intersection only keeps elements in both sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.intersection_update(setB) # 1 2 3
print(setA)
# Symmetric intersection only keeps elements in both sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.symmetric_difference(setB) # keep 1 to 9
print(setA)

# Subsets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3}
print(setB.issubset(setA))
print(setA.issubset(setB))
# supersets
print(setB.issuperset(setA))
print(setA.issuperset(setB))
# disjoints
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3}
setC = {10, 11, 12}
print(setB.isdisjoint(setA))
print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))
# copy
setD = setA.copy() # no mods to setA
setD = {1,2}
print(setA)
print(setD)
# Frozen immutable
frozeSet = frozenset({1, 2, 3, 5, 6, 7})
print(frozeSet)







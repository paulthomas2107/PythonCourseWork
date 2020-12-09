# Tuples (immutable)

import sys
import timeit

listA = [0, 1, 2, 'hello', True]
tupleA = [0, 1, 2, 'hello', True]
print(sys.getsizeof(listA), "bytes")
print(sys.getsizeof(tupleA), "bytes")

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))


myTuple = ("Max", 28, "Boston")
print(myTuple)
anotherTuple = tuple(["1", 22, 'Paul'])
print(anotherTuple)
print(type(anotherTuple))  # Tuple

print(myTuple[0])
print(myTuple[1:3])

for myTupleItem in myTuple:
    print(myTupleItem)

if "Max" in myTuple:
    print("Max found")
else:
    print("nope...")

tuple2 = ('a', 'p', 'p', 'l', 'e')
print(len(tuple2))
print(tuple2.count('p'))
print(tuple2.index('p'))

myList = list(myTuple)
print(myList)
myNewTuple = tuple(myList)
print(myNewTuple)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(b)
b = a[::2]
print(b)
b = a[::-1]
print(b)

newTuple = "Paul", 21, "Manchester"
name, age, city = newTuple
print(name, age, city)

anotherTuple = (0, 2, 4, 5, 6, 10, 12)
i1, *i2,  i3 = anotherTuple
print(i1)
print(i2)
print(i3)

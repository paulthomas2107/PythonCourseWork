from functools import reduce

add10 = lambda x: x + 10

print(add10(9))


def add_ten(x):
    return x + 10


print(add_ten(21))


def multi(x, y):
    return x * y


mult = lambda x, y: x * y
print(mult(10, 20))
print(multi(10, 20))


def sort_by_y(x):
    return x[1]


points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D)
print(points2D_sorted)

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=sort_by_y)
print(points2D)
print(points2D_sorted)

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D)
print(points2D_sorted)

# map (function, sequence)
a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x * 2, a)
print(list(b))

c = [x * 2 for x in a]
print(c)

# filter
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

# same as
c = [x for x in a if x % 2 == 0]
print(list(c))

# Reduce
a = [1, 2, 3, 4, 5, 6]
productA = reduce(lambda x, y: x * y, a)
print(productA)

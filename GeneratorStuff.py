# Generator - generates objects that can be iterated over
import sys


def my_generator():
    yield 5
    yield 2
    yield 1


"""
g = my_generator()
for i in g:
    print(i)
"""

g = my_generator()
x = next(g)
print(x)
x = next(g)
print(x)
x = next(g)

g = my_generator()
print(sum(g))

g = my_generator()
print(sorted(g))


def countdown(num):
    print('Start....')
    while num > 0:
        yield num
        num -= 1


cd = countdown(4)
value = next(cd)
print(next(cd))
print(next(cd))


def first_num(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sys.getsizeof(first_num(10)))


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(30)
for i in fib:
    print(i)


my_gen = (i for i in range(10) if i % 2 == 0)
for i in my_gen:
    print(i)

my_gen = (i for i in range(10) if i % 2 == 0)
print(list(my_gen))
print(sys.getsizeof(my_gen))


my_list = [i for i in range(10) if i % 2 == 0]
print(my_list)
print(sys.getsizeof(my_list))




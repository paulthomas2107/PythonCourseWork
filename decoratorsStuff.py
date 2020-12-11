# Function and Class Decorators
import functools


# Function

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        results = func(*args, **kwargs)
        print('End')
        return results
    return wrapper


@my_decorator
def do_stuff():
    print('Paul Thomas ' * 2)


@my_decorator
def add5(x):
    return x + 5


# Call wrapped method
do_stuff()
result = add5(10)
print(result)

print(help(add5))
print(add5.__name__)


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                res = func(*args, **kwargs)
            return res
        return wrapper
    return decorator_repeat


# a decorator function that prints debug information about the wrapped function
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        res = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {res!r}")
        return res
    return wrapper


@repeat(num_times=8)
def greet(name):
    print(f'Hello {name}')


greet('Paul')
print('-' * 50)


@debug
@my_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting


say_hello('Paulie')
print('-' * 50)


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'Number of calls {self.num_calls}')
        return self.func(*args, **kwargs)


@CountCalls
def another_hello():
    print('Hello')


another_hello()
another_hello()




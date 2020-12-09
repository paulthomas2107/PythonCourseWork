# Exceptions
"""
x = -5

if x < 0:
    raise Exception('X should be positive')




print('-' * 100)
x = -1
assert (x > 200), 'x is not positive'
print('-' * 100)

"""
try:
    a = 5 / 0
    b = 10 / 2
    b = b + 1
except ZeroDivisionError as e:
    print('Error found:', e)
except TypeError as e:
    print('Error found:', e)
else:
    print('All good above...')
finally:
    print('Clearing up......')
print('-' * 100)


# create our own exception
class ValueWayTooHighException(Exception):
    pass


class ValueTooSmallException(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_val(x):
    if x > 100:
        raise ValueWayTooHighException('Way too big')
    if x < 50:
        raise ValueTooSmallException('Way too SMALL', x)


try:
    test_val(49)
except ValueWayTooHighException as e:
    print('Error:', e)
except ValueTooSmallException as e:
    print('Error:', e)

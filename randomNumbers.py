import random
import secrets
import numpy as np

# Pseudo random

a = random.random()  # 0 to 1
print(a)

a = random.uniform(1, 100)  # float with range
print(a)

a = random.randint(1, 100)  # integer`with range
print(a)

a = random.randrange(1, 100)  # never picks 100
print(a)

a = random.normalvariate(0, 1)
print(a)

lister = list("ABCDEF")
a = random.choice(lister)
print(a)

a = random.sample(lister, 3)
print(a)

a = random.choices(lister, k=3)
print(a)

random.shuffle(lister)
print(lister)


# Secrets - more secure
a = secrets.randbelow(256)
print(a)

a = secrets.randbits(16)  # 1 to 65535
print(a)

lister = list('ABCDEFGHIJK')
a = secrets.choice(lister)
print(a)

# numpy
a = np.random.randint(2, 256, 8)
print(a)
print(a[0:3])

# With tuple
print('=' * 50)
a = np.random.randint(0, 256, (3, 4))
print(a)

# with shuffle
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr)
print(arr)








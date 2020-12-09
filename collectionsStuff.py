from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter
aList = Counter('aaaaaaannnnnnnnvvvvvvvm')
print(aList)
print(aList.keys())
print(aList.values())
print(aList.most_common())
print(aList.most_common(1))  # most common
print(aList.most_common(1)[0][0])  # most common letter
print(list(aList.elements()))

# Named Tuple
Point = namedtuple('Point', 'x,y')
pt = Point(217, 66)
print(pt)
print(pt.x)
print(pt.y)

# Ordered Dictionary
orderedDic = OrderedDict()
orderedDic['name'] = 'Paul'
orderedDic['address'] = 'www.bbc.co.uk'
orderedDic['age'] = 22
orderedDic['phone'] = '020 121 1111'
print(orderedDic)
# or
orderedDic = {'name': 'Paul1', 'address': 'www1.bbc.co.uk', 'age': 221, 'phone': '0201 121 1111'}
print(orderedDic)

# Default Dictionary
defDic = defaultdict(int)  # default of int if not supplied
defDic['a'] = 1
defDic['b'] = 2
print(defDic)

# Deque - double ended queue
d = deque()
d.append(1)
d.append('Paul')
print(d)
d.appendleft(217)
d.appendleft(0)
print(d)
d.pop()  # last element popped off
print(d)
d.popleft()  # last element popped off
print(d)
d.extend([100, 200, 299])
print(d)
d.extendleft([-100, -200, -300])
print(d)
d.rotate(1) # rotate right
print(d)
d.rotate(-2) # rotate left
print(d)
d.clear() # empty
print(d)










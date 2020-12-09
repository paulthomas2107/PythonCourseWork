# Immutable (cant be changed)
import timeit

m1 = 'Paul'
# or double quotes
m2 = "Paul Thomas is my name"

print(m2)
charPos = m2[1]  # a
print(charPos)
charPos = m2[-1]  # s
print(charPos)
chunk = m2[2:8]  # from 2 to 8
print(m2[1:])  # from 1
print(m2[:8])  # to 8
print(m2[::2])  # every 2nd char
print(m2[3::2])  # every 2nd char after 3rd
print(m2[::-1])  # reverse whole string

firstName = "Paul"
lastName = "Thomas"
fullName = firstName + " " + lastName
print(fullName)

for part in fullName:  # every letter in full name
    print(part)

if 'a' in fullName:
    print("Yes..")

if 'q' not in fullName:
    print("Q not found")

whiteSpace = '   hello World  end'
print(whiteSpace)
whiteSpace = whiteSpace.strip()
print(whiteSpace)
whiteSpace = whiteSpace.strip('end')   # strip end off
print(whiteSpace)

# Checks
print(whiteSpace.capitalize())
print(whiteSpace.upper())
print(whiteSpace.lower())
print(whiteSpace.startswith('h'))
print(whiteSpace.endswith('rld'))
locO = whiteSpace.find('l')
print(locO)
locO = whiteSpace.find('lo W')
print(locO)
locO = whiteSpace.find('NOT FOUND')
print(locO)  # -1 not found
countOfLL = whiteSpace.count('l')
print(countOfLL)
whiteSpace = 'Hello World'
print(whiteSpace.replace('Hello', 'Books'))

# Split out after 'SPACE'
myString = 'How are you doing'
myList = myString.split()
print(myList)

for aWord in myList:
    print(aWord)

# Split out after '+'
myString = 'How+are+you+doing'
myList = myString.split('+')
print(myList)

for aWord in myList:
    print(aWord)

# convert list back to string
newString = ''.join(myList)
print(newString)

myList = ['pt'] * 10
print(myList)

# Show time to join
start = timeit.default_timer()
myString = ''.join(myList)
stop = timeit.default_timer()
print(stop - start)

# Formatting Strings
# Old way
var = "Paul"
myString = "the variable is %s" % var
print(myString)
var = 217
myString = "the variable is %d" % var
print(myString)
var = 217.222
myString = "the variable is %.2f" % var  # to 2 dec points
print(myString)

# NEW WAY
# ---------
var = "Paul"
myString = "Your name is {}".format(var)
print(myString)
var = 3.1423321123
heightS = 6.2123233
myString = "Your name is %.2f" % var
print(myString)
# or newer
var = 3.1423321123
heightS = 6.2123233
myString = "Your name is {:.2f} and {:.3f}".format(var, heightS)
print(myString)

# Latest
var = 3.14322
var2 = 12
myOther = f"Your name is {var} and {var2}"  # 3 decimal places and then 2
print(myOther)



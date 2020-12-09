# Key pair structure
myDic = {"key": "data"}
print(myDic)
myDic = {"car": "ford", "bike": "raleigh", "Ricky": "Gervais"}
print(myDic)
# or
myDic = dict(name="Paul", town="London", country="UK", age=19)
print(myDic)
print(myDic["town"])
print(myDic["age"])
# add to existing dictionary
myDic["additional"] = "Europe"
print(myDic)
# update a value
myDic["town"] = "Berlin"
print(myDic)
# remove item
del myDic["age"]
print(myDic)
# also removes
myDic.pop("town")
print(myDic)
# removes last item
myDic.popitem();
print(myDic)
# reset
myDic = dict(name="Paul", town="London", country="UK", age=19)

if "town" in myDic:
    print("Town found - ", myDic["town"])

try:
    print(myDic["NULL"])
except:
    print('Not found')

# loop over keys/value
for key in myDic.keys():
    print(key)
for value in myDic.values():
    print(value)
# both
for key, value in myDic.items():
    print(key, value)

# copy
myDicCopy = myDic
myDicCopy["new"] = 'Added'
# original copied via copy
print(myDic)
# original wont change
myDicCopy = myDic.copy()
myDicCopy["address"] = "house"
print(myDic)
print(myDicCopy)
# or this original wont change
myDicCopy = dict(myDic)
myDicCopy["address"] = "house"
print(myDic)
print(myDicCopy)

# merging two dictionaries
myDic3 = {"Song": "Hello", "age": 100}
myDic4 = dict(composer="Bach", location="Salzberg", age=250)
myDic3.update(myDic4)
print(myDic3)

# key types
myDic = {3: 6, 9: 81, 122: 999}
print(myDic)
print(myDic[122])
# using tuple as key
myTuple = (21, 1)
myDic = {myTuple: 222}
print(myDic)


















# Lists
myList = ["banana", "apple", "orange"]
print(myList)
myList2 = list()
myList2.append("Cheese")
myList2.append("grapes")
print(myList2)
myList3 = [True, "dog", 123.45]
print(myList3)
print(myList3[len(myList3)-1])

for item in myList3:
    print('Item : ', item)

if "dog" in myList3:
    print("Dog found")
else:
    print("Not found..")

print(len(myList3))
myList3.insert(1, "cat")
print(myList3)
removedItem = myList3.pop(3)
print(myList3)
print('Removed: ', removedItem)
myList3.reverse()
print(myList3)
myList3.clear()
print(len(myList3))
myList4 = [100, 12, 1, 56, 333, 2]
sortedList = sorted(myList4)
print(myList4)
print(sortedList)

myList5 = ["paul"] * 3, 1, 2, 4
print(myList5)

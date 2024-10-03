thislist = ["apple", "banana", "cherry"]

# removed item from last index using pop() method
thislist.pop()
print(thislist) # out will be ["apple","banana"]. Because pop method removed "cherry" item

# removed as list item index wise using pop(index)
thislist.pop(1)
print(thislist) # this list will be ["apple"]. pop(1) removed list[1] item


# delete as value wise from list item = using remove("item value")
thislist.remove("apple")
print(thislist) # output will be blank list


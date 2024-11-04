arr = [80, 70, 10, 20, 30, 40, 50]
print(arr)
# update array element at index
arr[3] = 2000
print(arr)

# insert array element at end
arr.append(100)
print(arr)

# insert array element at end
arr.insert(2, 5)
print(arr)

# Removed array element as element value wise
arr.remove(2000) 
print(arr)

# Removed array element at index 
arr.pop(2)
print(arr)

# removed full array 
# arr.clear()

# Search array element
if 30 in arr:
    print(arr.index(30))
    print(True)

# Traversing the array -   Loop through each element in the array to perform operations
for element in arr:
    print(element)

# copy array 
newArr = arr.copy()

# sorting array
newArr.sort()
print(newArr)
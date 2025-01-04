import array

arr = [80, 70, 10, 20, 30, 40, 50]

# array crud 

# insert array element
arr.append(1000)
arr.insert(2, 100)
arr.extend([200, 300, 400]) # add multiple elements at the end of the array

arr2 = [500, 600, 700]
arr += arr2 # add multiple elements at the end of the array

for i in range(len(arr)):
    print(arr[i])


# update array element at index
arr[3] = 2000
arr[0:1] = [5000, 6000] # update multiple elements at the same time
print("Array after update")

for i in range(len(arr)):
    print(arr[i])


# Removed array element as element value wise
arr.remove(5000)     
arr.pop(2) # Removed array element at index
# arr.clear() # removed full array

print("Array after remove")

for i in range(len(arr)):
    print(arr[i])   
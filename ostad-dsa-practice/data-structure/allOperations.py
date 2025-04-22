# Practices commond operations on Data Structure
# Traversal = visting each element by element 
# Insersion , Deletion, Searching, Sorting and Marging 

list = [10, 8 ,7,55,80,4,2,79,88,99,100,15,20,25,30,47]

# array traversal operation
def ArrayTraversal(arr):
    result = 0
    for i in range(len(arr)):
        result += arr[i]
    return result

# Array insertion
def ArrayInsertion(arr, value):
    arr.insert( len(arr)+1,value)
    return arr

# Array deletion 
def ArrayDeletion(arr , target):
    for i in range(len(arr)):
        if arr[i] == target:
            arr.pop(i)
    return arr

# Array Searching Element 
def ArraySearching(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

# Array sortin: bubble sort
def ArraySorting(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

# Array Merge
def ArrayMerge(arr1, arr2):
    return arr1 + arr2
  
sortedArray = ArraySorting(list)
newArray = ArrayMerge(list, sortedArray)         

print(list)
print(newArray)
print(ArrayTraversal(list))
print(ArrayInsertion(list,40))
print(ArrayDeletion(list, 40))
print(ArraySearching(list, 20))
print(ArraySorting(list))
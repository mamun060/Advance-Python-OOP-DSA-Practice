# Linear search work on sorted and unsorted arrays
# It is a simple search algorithm that checks each element in the list one by one until the desired element is found or the end of the list is reached.
# It has a time complexity of O(n), where n is the number of elements in the list.

def Linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

list = [1, 2, 3, 4, 5]
target = 3
result = Linear_search(list, target)
print("Element found at index:", result)
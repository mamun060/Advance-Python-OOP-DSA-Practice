#Ternary search is a divided and conquer based algorithm that works on sorted arrays
# Three devided the array instead of two like binary search

def ternary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid1 = start + ( end - start) // 3
        mid2 = end - ( end - start ) // 3
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        if target < arr[mid1]:
            end = mid1 - 1
        elif target > arr[mid2]:
            start = mid2 + 1
        else:
            start = mid1 + 1
    return -1

list = [1, 2, 3, 4, 5]
target = 3
result = ternary_search(list, target)
print("Element found at index:", result)
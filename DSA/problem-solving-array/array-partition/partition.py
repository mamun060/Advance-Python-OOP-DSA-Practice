def partition(arr, n):
    middle = len(arr) // n
    return [arr[i:i + middle] for i in range(0, len(arr), middle)]

arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2
print(partition(arr, n)) # [[1, 2, 3, 4], [5, 6, 7, 8]]
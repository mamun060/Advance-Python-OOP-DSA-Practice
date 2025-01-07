def equatPartition(arr, n):
    size = len(arr) // n
    return [arr[i:i + size] for i in range(0, len(arr), size)]

arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2
print(equatPartition(arr, n)) # [[1, 2, 3, 4], [5, 6, 7, 8]]
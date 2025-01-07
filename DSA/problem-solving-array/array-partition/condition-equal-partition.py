def conditionalPartition(arr, n):
    even = [arr[i] for i in range(0, len(arr), 2)]
    odd = [arr[i] for i in range(1, len(arr), 2)]
    return [even, odd]

arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2
print(conditionalPartition(arr, n))
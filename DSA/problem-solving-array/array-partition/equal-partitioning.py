def equalPartion(arr, n):
    middleSize = len(arr) // n
    return [arr[i:i + middleSize] for i in range(0, len(arr), middleSize)]

arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2
print(equalPartion(arr, n)) # [[1, 2, 3, 4], [5, 6, 7, 8]]
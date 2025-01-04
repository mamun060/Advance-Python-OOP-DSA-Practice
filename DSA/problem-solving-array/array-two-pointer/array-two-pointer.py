arr = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8, 9, 10]

target = 15

def two_pointer(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum == target:
            return ( arr[left], arr[right])
        elif currentSum < target:
            left = left + 1
        else:
            right = right - 1
    return None

print(two_pointer(arr, target))

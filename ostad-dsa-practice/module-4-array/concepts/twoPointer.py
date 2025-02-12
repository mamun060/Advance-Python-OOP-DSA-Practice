def twoPointer(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return None


arr = [1, 2, 3, 4, 6, 8, 9]

target = 10
result = twoPointer(arr, target)
print(result)
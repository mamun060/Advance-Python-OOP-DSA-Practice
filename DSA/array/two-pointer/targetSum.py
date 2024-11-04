def find_pair(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None


arr = [10, 30, 40, 50, 70, 80, 100]
target = 60
print(find_pair(arr, target))
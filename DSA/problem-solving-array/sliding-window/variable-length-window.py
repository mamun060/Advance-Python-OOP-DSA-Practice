# smallest subarray with sum greater than a given value

def smallest_subarray(arr, target):
    n = len(arr)
    start = 0
    current_sum = 0
    min_length = float('inf')

    for end in range(n):
        current_sum = current_sum + arr[end]
        while current_sum >= target:
            min_length = min(min_length, end - start + 1)
            current_sum = current_sum - arr[start]
            start = start + 1
    return min_length if min_length != float('inf') else 0

arr = [2, 3, 1, 2, 4, 3]
target = 7
print(smallest_subarray(arr, target))

# max sum of subarray of variable Length
def max_sum_subarray(arr, target):
    start = 0
    current_sum = 0
    max_sum = float('-inf')

    for end in range(len(arr)):
        current_sum = current_sum + arr[end]
        
        if end - start + 1 > target:
            current_sum = current_sum - arr[start]
            start = start + 1
        max_sum = max(max_sum, current_sum)
    return max_sum

arr = [1, 2, 3, -2, 5]
k = 3
print(max_sum_subarray(arr, k)) 
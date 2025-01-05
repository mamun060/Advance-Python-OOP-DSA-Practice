# Fixed window sliding technique

def fixed_window(arr, k):
    max_sum = 0
    window_sum = 0

    if len(arr) < k:
        return None
    
    for i in range(k):
        window_sum += arr[i]
    max_sum = window_sum


    for i in range (k, len(arr)):
        window_sum = window_sum + arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
print(fixed_window(arr, k)) # 18
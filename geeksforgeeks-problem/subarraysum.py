class Solution:
    def subArraySum(self, arr, target):
        cumulative_sum = 0
        sum_index = {}
        for x in range(len(arr)):
            cumulative_sum += arr[x]
            if cumulative_sum == target:
                return [1, x + 1]
            if (cumulative_sum - target) in sum_index:
                start_index = sum_index[cumulative_sum - target]
                return [start_index + 2, x + 1]
            sum_index[cumulative_sum] = x
        return None

#Another way to save run time error
class SolutionTwo:
    def subArraySum(self, arr, target):
        start,end=0,0
        while(True):
            if sum(arr[start:end+1])<target and end<len(arr)-1:
                end+=1
            elif sum(arr[start:end+1])>target and start<=end:
                start+=1
                if start>end :
                    end+=1
            else :
              if sum(arr[start:end+1])==target:
                return [start+1,end+1]
              else :
                  return [-1]
            if start>end:    
                return [-1]

arr = [1,2,3,4,5,6,7,8,9,10]
target = 15
obj = SolutionTwo()
result = obj.subArraySum(arr, target)
print(result)

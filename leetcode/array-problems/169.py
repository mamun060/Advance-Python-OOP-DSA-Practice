# Leetcode: 169 problem. Majority Element

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        for key, value in dic.items():
            if value > len(nums) // 2:
                return key
        return None
    

Solution = Solution()
print(Solution.majorityElement([3,2,3])) # 3
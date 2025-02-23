# Leetcode: 217 problem. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) != len(set(nums)):
            return True
        return False  

Solution = Solution()
print(Solution.containsDuplicate([1,2,3,1]))
print(Solution.containsDuplicate([1,2,3,4]))
print(Solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
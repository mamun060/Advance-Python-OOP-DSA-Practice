# Leetcode: 88 problem. Merge Sorted Array
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        """
        nums1[m:] = nums2[:n]
        nums1.sort()
        return nums1
    

arr1 = [1,2,3,0,0,0]
arr2 = [2,5,6]
arr1[3:] = arr2[:3]
print(sorted(arr1))

Solution = Solution()
print(Solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
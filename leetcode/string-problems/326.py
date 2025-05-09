# power of three
# class Solution:
#     def isPowerOfThree(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         if n == 0:
#             return False
#         while n % 3 == 0:
#             n /= 3
#         return n == 1

# Solution = Solution()
# print(Solution.isPowerOfThree(27))


def powerofthree(n):
    if n == 0:
        return False
    while n % 3 == 0:
        n = n / 3
    return n == 1

print(powerofthree(-1))
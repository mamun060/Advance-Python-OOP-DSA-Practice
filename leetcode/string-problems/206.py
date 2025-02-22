# Leetcode:206 problem. Reverse Linked List
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            temp = head
            head = head
            temp = prev
            prev = temp
        return prev
    

Solution = Solution()
print(Solution.reverseList([1,2,3,4,5]))
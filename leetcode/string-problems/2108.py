# Problem: Find the first palindrome in a list of words
# Given a list of words, return the first word that is a palindrome (reads the same forwards and backwards). If no word is a palindrome, return None.

class Solution:
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            if word == word[::-1]:
                return word
        return
    
words = ["def","ghi"]
s = Solution()
print(s.firstPalindrome(words))
# check weather two strings are almost equivalent or not
# two strings are almost equivalent if they have same characters but in different order

class Solution:
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """ 
        freequency1 = {}
        freequency2 = {}
        for char in word1:
            if char in freequency1:
                freequency1[char] += 1
            else:
                freequency1[char] = 1
        
        for char in word2:
            if char in freequency2:
                freequency2[char] += 1
            else:
                freequency2[char] = 1

        for letter in set(word1 + word2):
            if abs(freequency1.get(letter, 0) - freequency2.get(letter, 0)) > 3:
                return False
        return True 
        
    
a = "zzzyyy"
b = "iiiiii"
s = Solution()
print(s.checkAlmostEquivalent(a, b))
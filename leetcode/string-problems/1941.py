class Solution:
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    
        first_freq = freq[s[0]]
        
        for char in freq:
            if freq[char] != first_freq:
                return False
        
        return True
        

name = "raaju"
char_freq = {}
for char in name:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

print(char_freq[name[0]])
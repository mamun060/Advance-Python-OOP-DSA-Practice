# Capitalize the title 

class Solution:
    def capitalize(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = title.split()
        result = [words[0].capitalize()]
        for word in words[1:]:
            if word.lower() in ['and', 'the', 'of', 'in']:
                result.append(word.lower())
            else:
                result.append(word.capitalize())
        return ' '.join(result)

title = "First leTTeR of EACH Word"
print(Solution().capitalize(title)) 
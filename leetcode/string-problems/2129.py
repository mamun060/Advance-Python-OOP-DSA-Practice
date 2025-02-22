# Capitalize the title 

class Solution:
    def capitalize(self, title):
        """
        :type title: str
        :rtype: str
        """
        output = list()
        word_arr = title.split()
        for word in word_arr:
                output.append(word.title()) if len(word) > 2 else output.append(word.lower())
        return " ".join(output)

Solution = Solution()

# Test Cases
print(Solution.capitalize("i lOve leetcode"))
print(Solution.capitalize("capiTalIze tHe titLe"))
print(Solution.capitalize("First leTTeR of EACH Word"))
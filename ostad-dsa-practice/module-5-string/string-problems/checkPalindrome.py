def checkPalindrome(s: str)-> str:
    if s == s[::-1]:
        return "YES"
    else:
        return "NO"

s = input().strip()
print(checkPalindrome(s))
print(checkPalindrome("ostad"))
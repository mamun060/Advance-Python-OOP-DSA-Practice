def checkPalindrome(s):
    if s != s[::-1]:
        return f"{s} is not a palindrome"
    return f"{s} is a palindrome"

print(checkPalindrome("madam"))
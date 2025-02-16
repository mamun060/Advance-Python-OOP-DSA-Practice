def shortestPalindrome(s):
    if not s:
        return s
    s_reverse = s[::-1]
    new_s = s + '#' + s_reverse
    lps = [0] * len(new_s)
    j = 0

    for i in range(1, len(new_s)):
        while j > 0 and new_s[i] != new_s[j]:
            j = lps[j - 1] 
        if new_s[i] == new_s[j]:
            j += 1
            lps[i] = j
    extra_chars = s_reverse[:len(s) - lps[-1]]
    return extra_chars + s


s = input().strip()
print(shortestPalindrome(s))

def rotateString(s):
    for i in range(len(s)):
        s = s[1:] + s[0]
        return s

s = input().strip()
print(rotateString(s))
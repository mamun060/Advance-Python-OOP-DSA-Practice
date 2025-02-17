def maxFrequency(s: str) -> str:
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    maxChar = ''
    maxCount = 0
    for char, count in frequency.items():
        if count > maxCount:
            maxChar = char
            maxCount = count
        elif count == maxCount and char < maxChar:
            maxChar = char
    return f"{maxChar} {maxCount}"

s = input().strip()
print(maxFrequency(s))

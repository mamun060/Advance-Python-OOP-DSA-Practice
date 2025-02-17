def maxFrequency(s: str) -> str:
    sortedS = sorted(s)
    maxChar = max(sortedS, key = sortedS.count)
    charLen = sortedS.count(maxChar)
    return f"{maxChar} {charLen}"

s =input().strip()
print(maxFrequency(s))
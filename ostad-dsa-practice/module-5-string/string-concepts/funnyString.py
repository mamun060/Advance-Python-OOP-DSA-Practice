def is_funny(S: str) -> str:
    for i, c in enumerate(S):
        if i % 2 == 0:  # Odd-positioned characters (1st, 3rd, ...)
            if not c.islower():
                return "No"
        else:  # Even-positioned characters (2nd, 4th, ...)
            if not c.isupper():
                return "No"
    return "Yes"

S = input().strip()
print(is_funny(S))

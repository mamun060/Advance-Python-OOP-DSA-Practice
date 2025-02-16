def is_funny(S: str) -> str:
    for i in range(len(S)):
        if (i % 2 == 0 and not S[i].islower()) or (i % 2 == 1 and not S[i].isupper()):
            return "No"
    return "Yes"

S = input().strip()
print(is_funny(S))

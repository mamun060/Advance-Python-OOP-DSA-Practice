def is_anagram(A: str, B: str) -> str:
    if sorted(A) == sorted(B):
        return "YES"
    else:
        return "NO"

# A = input().strip()
# B = input().strip()
A = "abcd"
B = "dbac"

print(sorted(B))

print(is_anagram(A, B))

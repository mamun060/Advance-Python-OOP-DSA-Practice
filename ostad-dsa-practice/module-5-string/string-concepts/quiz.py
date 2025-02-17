#1 
raju  =  "Hello, World!"
print(len(raju))

# 2 
s = "abc"
s = s[:1] + 'z' + s[2:]
print(s)

# 8 
def is_palindrome(s: str) -> bool:
    cleaned_s = ""
    for char in s:
        if char.isalnum():
            cleaned_s += char.lower()
    return cleaned_s == cleaned_s[::-1]

sentence = "Hello world, welcome to coding."
if is_palindrome(sentence):
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")

# 9 check anagram 
def is_anagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

a = "dog"
b = "god"
print(is_anagram(a, b))
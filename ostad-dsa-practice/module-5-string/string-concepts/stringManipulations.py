# using silicing [::-1] for reverse string

full = "Ayhsa Akter"
reverse = full[::-1]
print(reverse)
print(reverse[::-1])

# Using reversed() function and join() method
fullName = "John Doe"
ultoName = "".join(reversed(fullName))
print(ultoName)

# String reverse using for loop
reversedChar = ""
for i in fullName:
    reversedChar = i + reversedChar

print(reversedChar)

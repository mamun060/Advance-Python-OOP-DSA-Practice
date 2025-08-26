# abs() -> Returns the absolute value of a number
integer = -20
print(abs(integer))  # Output: 20

# all() - Returns True if all elements of the iterable are true (or if the iterable is empty).
k = [1, 2, 3] # List of integers - mane sequence tikh takhte hobe either false, if sequence is okay then true
print(all([True, True, False]))  # Output: False
print(all(k))  # Output: True

# bin() - Converts an integer to a binary string.
num = 8
print(bin(num))  # Output: 0b1000

#The python bool() converts a value to boolean(True or False) using the standard truth testing procedure.
test1 = []
print(bool(test1))  # Output: False

test2 = [0]
print(bool(test2))  # Output: True

test3 = [1]
print(bool(test3))  # Output: True

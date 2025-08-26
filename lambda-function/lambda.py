# Lambda function in python is a anonymous function expressed as a single statement.
# Lambda function take n number of arguments but return only one value.
add = lambda x, y : x + y
print(add(5, 10))  # Output: 15

subtract = lambda x, y, c: x - y - c
print(subtract(10, 5, 2))  # Output: 3

numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]      
squared_list = list(map(lambda x: x**2, numbers_list))  # squaring each number in the list
print(squared_list)


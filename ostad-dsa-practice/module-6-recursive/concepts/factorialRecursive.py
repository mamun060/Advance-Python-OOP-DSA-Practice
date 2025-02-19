# Factorial Using Recursion
def Factorial(n):
    if n == 1:
        return 1
    return n * Factorial(n-1)

print(Factorial(5)) 

# Factorial Using loop
def factorialLoop(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

print(factorialLoop(5))

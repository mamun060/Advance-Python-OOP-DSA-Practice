def recursion(n):
    if n == 4:
        return n
    else:
        return 2 * recursion(n+1)

print(recursion(2))

def fun(x,y):
    if y == 0:
        return 0
    return x + fun(x, y-1)
print(fun(3,4))  

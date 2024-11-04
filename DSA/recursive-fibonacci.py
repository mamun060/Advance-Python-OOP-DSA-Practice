prev1 = 1
prev2 = 0
count = 2

def Fibonacci(preview1 , preview2):
    global count
    if count <= 19:
        newFibo = preview1 + preview2
        print(newFibo)
        preview2 = preview1
        preview1 = newFibo
        count += 1
        Fibonacci(preview1 , preview2)
    else:
        return 

Fibonacci(1,0)
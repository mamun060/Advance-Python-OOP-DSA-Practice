def Recursive(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    Recursive(n-1) # Recursive call

Recursive(5)
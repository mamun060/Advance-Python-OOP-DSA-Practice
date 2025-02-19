def Recursive(n):
    if n == 0:
        print("Done!")
        return
    Recursive(n-1) # Recursive call
    print(n)

Recursive(5)


# using class 
class Recursive:
    def __init__(self, n):
        self.n = n
        if n == 0:
            print("Done!")
            return
        print(n)
        Recursive(n-1)

Recursive(4)
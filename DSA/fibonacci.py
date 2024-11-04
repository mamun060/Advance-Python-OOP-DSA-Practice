class Fibonacci:
    def fibo(self , length):
        prev1 = 1
        prev2 = 0
        print(prev1)
        print(prev2)
        for i in range(length):
            count = prev1 + prev2
            print(count)
            prev2 = prev1
            prev1 = count

fiboObject = Fibonacci()
fiboObject.fibo(10)
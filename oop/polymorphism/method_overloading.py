# method overload - means having multiple methods with the same name but different parameters

class Math:
    def add(self, a, b = 0, c = 0) -> float:
        return a + b + c

match = Math()
print(match.add(5))          # Output: 5
print(match.add(5, 10))      # Output: 15
print(match.add(5, 10, 15))  # Output: 30
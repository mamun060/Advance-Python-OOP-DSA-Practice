### Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

```python
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x is not z)
print(x is not y)

```
#Tuples are unchangeable or immutable, so if we need to update tuples items?
# we need to conver tuples to list then we can update items 

mytuple = ('cherry', 'orange', 'kiwi')
mylist = list(mytuple)
mylist[0] = "Banana"

# then the updated list assigned to tuple
mytuple = tuple(mylist)

print(mytuple)
print(mylist)
my_List = [ [3, 5, 8, 6], [23, 54, 12, 87], [1, 2, 4, 12, 5] ]   
sort_list = lambda x: (sorted(i) for i in x)
print(list(sort_list(my_List)))

# Getting the third largest number of the sublist    
third_Largest = lambda num, func : [ l[ len(l) - 3] for l in func(num)]    
result = third_Largest( my_List, sort_list)      
print('The third largest number from every sub list is:', result )    
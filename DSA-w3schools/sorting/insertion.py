class InsertionSort:
    def insertion(self, arr):
        for i in range(len(arr)):
            for j in range(i , len(arr)):
                if arr[i] > arr[j] and arr[i+1] > arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
        return arr
    
arr = [ 9, 7, 8, 4, 65, 4, 5, 5, 84, 8, 99, 10, 11, 144, 150]
insertionObject = InsertionSort()
print(insertionObject.insertion(arr))
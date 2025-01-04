class SelectionSort:
    def selection(self, arr):
        for i in range(len(arr)-1):
            minIndex = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            temp = arr[i]
            arr[i] = arr[minIndex]
            arr[minIndex] = temp
        return arr


list = [ 9, 7, 8, 4, 65, 4, 5, 5, 84, 8, 99, 10, 11, 144, 150]
selectObject = SelectionSort()
print(selectObject.selection(list))

class BubbleSort:
    def bubble(self, arr):
        for i in range(len(arr) - 1):
            for j in range(1, len(arr) - i):
                if arr[j - 1] > arr[j]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]
        return arr


list = [5,8,7,9,45]
bubbleObject = BubbleSort()
print(bubbleObject.bubble(list))
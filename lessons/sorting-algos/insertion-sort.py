def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            # arr[j] and arr[j + 1] are out of order, so swap them
            temp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = temp
            j -= 1
    return arr

words = ["apple", "grape", "banana", "clemintime"]
sorted_words = insertionSort(words)
print(sorted_words)

someNums = [1, 2, 3, 44, 22, 15, 9]
sorted_nums = insertionSort(someNums)
print(someNums)
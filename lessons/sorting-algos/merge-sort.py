def mergeSort(arr, s, e):
    if e - s + 1 <= 1:
        return arr
    
    # The iddle index of the array
    m = (s + e) //2

    # sort the left half
    mergeSort(arr, s, m)

    # sort the right half 
    mergeSort(arr, m + 1, e)

    # merge sorted halves
    merge(arr, s, m, e)

    return arr

# Merge in place
def merge(arr, s, m, e):
    L = arr[s: m + 1]
    R = arr[m + 1: e + 1]

    i = 0
    j = 0
    k = s # index for the start of the array 

    # merge two sorted halves into the original array
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # one of the halves may still have elements remaining
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

someNums = [1000, 2, 31, 9, 202, 88, 3]
sorted_nums = mergeSort(someNums, 0, 7)
print(sorted_nums)

words = ["apple", "grape", "kiwi", "banana", "clemintime"]
sorted_words = mergeSort(words, 0, 4)
print(sorted_words)

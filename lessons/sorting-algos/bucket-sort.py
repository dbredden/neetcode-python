def bucketSort(arr):
    # assuming arr only contains 0, 1 or 2
    counts = [0, 0, 0]

    # count the quantity of each val in arr
    for n in arr:
        counts[n] += 1
    
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr
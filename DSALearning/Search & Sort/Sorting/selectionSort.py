# try to take smallest out of whole array put at starting
# adding lowest at the start then starting from next of it
def selectionSort(array: list):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
        print(array)
    return array

print(selectionSort([2, 23, 10, 1]))
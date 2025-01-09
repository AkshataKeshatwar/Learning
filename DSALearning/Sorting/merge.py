def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    mergeSort(L)
    mergeSort(R)
    merge(L, R, arr)

def merge(x, y, arr):
    len_l, len_r = len(x), len(y)
    i = j  = k = 0
    while i < len_l and j < len_r:
        if x[i] < y[j]:
            arr[k] = x[i]
            i += 1
        else:
            arr[k] =  y[j]
            j += 1
        k += 1

    while i < len_l:
        arr[k] = x[i]
        i += 1
        k += 1

    while j < len_r:
        arr[k] = y[j]
        j += 1
        k += 1

if __name__ == "__main__":
    '''arr = [5,34,6,55,76,23,7]
    x, y = [34,55,76,89], [4,54,77,90,99,101,203,400]
    arr = merge(x, y)
    print(arr)'''
    arr = [5,34,6,90,88, 55,76,23,7]
    len_arr = len(arr)
    mergeSort(arr)
    print(arr)
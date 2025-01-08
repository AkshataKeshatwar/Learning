import copy
def mergeSort(arr, l, r, dtype):
    if len(arr[l:r+1]) == 1:
        dtype ="end"
        #print(arr[l:r+1], l, r, dtype)
    if l < r:
        m = l + (r-l)//2
        mergeSort(arr, l, m, "left")
        mergeSort(arr, m+1, r, "right")
        merge(arr, l, m, r)

def merge(arr, l, m, r):
    L = copy.deepcopy(arr[l:m+1])
    R = copy.deepcopy(arr[m+1:r+1])
    

    i = 0
    j = 0
    k = l
    #print( L, i, m, R, j, r, arr)
    while i < len(L) and j < len(R):
        #print( {i}, "<", {len(L)}, "and", {j},  "<", {len(R)})
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < len(R) :
        arr[k] = R[j]
        j += 1
        k += 1

if __name__ == "__main__":
    arr = [5,34,6,55,76,23,7]
    len_arr = len(arr)
    mergeSort(arr, 0, len_arr-1, "node")
    print(arr)

def binarySearch(arr:list, s:int) -> int:
    i = 0
    j = len(arr)
    while i<= j:
        mid = i + (j-i)//2
        if s == arr[mid]:
            return mid
        elif s > arr[mid]:
            i = mid + 1
        elif s < arr[mid]:
            j = mid - 1
    return -1

index = binarySearch([2,4,5,6,7,18,23,22,14], 7)
print(index)


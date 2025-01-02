def quickSort(array:list) -> list:
    if len(array) <= 1:
        return array
    else:
        pivote = array[0]
        right = [arr for arr in array if arr < pivote]
        left = [arr for arr in array if arr > pivote] 
        return (quickSort(right) + [pivote]+ quickSort(left))
s = quickSort([1,-4,-1,3,5,4,7,6,3,7])
print(s)
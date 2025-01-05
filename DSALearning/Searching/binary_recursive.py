def binary_search(arr, start, end, x):
    mid = start + (end-start)//2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search(arr, start, mid, x)
    else:
        return binary_search(arr, mid, end, x)



if __name__ == "__main__":
    arr = [8,9,34,55,67,89,404,505,609]
    print("element found at index", binary_search(arr,0, len(arr), 505))
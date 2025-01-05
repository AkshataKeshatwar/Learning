def binary_search(arr, start, end, x):
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            end = mid
        else:
            start = mid



if __name__ == "__main__":
    arr = [8,9,34,55,67,89,404,505,609]
    print("element found at index", binary_search(arr,0, len(arr), 505))
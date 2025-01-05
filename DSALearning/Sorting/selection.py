# swap after finding min

def selection(arr):
    l = len(arr)
    for i in range(l-1):
        min_idx = i
        for j in range(i+1, l):
            if arr[j] < arr[min_idx]:
                min_idx = j       
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    print(selection([5,34,6,55,76,23,7]))
    print(selection([76,23,5,56,50, 33, 45,7]))
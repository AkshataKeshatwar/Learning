# keep on sorting array by going back after getting element one by one

def insertion(arr):
    
    if len(arr) <= 1:
        return "Already Sorted"
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

if __name__ == "__main__":
    print(insertion([5,34,6,55,76,23,7]))
    print(insertion([76,23,5,56,50, 33, 45,7]))
     
# swapping of element by comparing every time

def bubbleSort(arr):
    l =len(arr)-1
    for i in range(l):
        for j in range(l-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    print(bubbleSort([5,34,6,55,76,23,7]))
    print(bubbleSort([76,23,5,56,50, 33, 45,7]))
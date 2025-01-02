# compare first element with all other element and swap
# putting highest no at the end and so on
def bubbleSort(array:list) -> list:
    n = len(array)-1
    for i in range(n):
        for j in range(n-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                print(array)
        print()
    return array

print(bubbleSort([6,4,5,22,18,3,23,88,26,77,65]))

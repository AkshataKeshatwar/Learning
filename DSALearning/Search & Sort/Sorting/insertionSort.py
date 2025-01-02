# check subarray sorted or not then add it
# sorting first 2 , then first 3, then first 4 and so on till end
def insertionSort(array:list) -> list:
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] =array[j-1] , array[j]
            j = j-1
    return array

print(insertionSort([54,2,5,4,2,55,23,12,66,6,7]))
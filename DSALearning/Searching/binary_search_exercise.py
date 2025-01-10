"""

Binary Search Exercise
When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?

numbers = [1,4,6,9,10,5,7]

Find index of all the occurances of a number from sorted list

numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
number_to_find = 15  
This should return 5,6,7 as indices containing number 15 in the array

"""

def search_number_with_occurrences(arr, num):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start) //2
        if arr[mid] == num:
            i, j = mid+1, mid
            result = []
            while arr[j] == num:
                result.append(j)
                j -= 1

            while arr[i] == num:
                result.append(i)
                i += 1
        
            return sorted(result)
        elif num < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


if __name__ == "__main__":
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15 
    print("element found at index", search_number_with_occurrences(numbers,55))
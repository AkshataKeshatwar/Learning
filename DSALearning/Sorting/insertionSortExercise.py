"""
Exercise: Insertion Sort
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers in a sorted list.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2

"""

def get_sorted_sub_arr(arr, key):
    if len(arr) == 0:
        return [key]
    i = len(arr)-1
    while key < arr[i] and i >= 0:
        i -= 1
    return arr[:i+1]+[key]+arr[i+1:]

def running_median(arr):
    count = 0
    sorted_arr = []
    for i in range(len(arr)):
        count += 1
        sorted_arr =  get_sorted_sub_arr(sorted_arr, arr[i])
        median_idx = count//2
        if count % 2 == 1:
            median = sorted_arr[median_idx]
        else:
            median = (sorted_arr[median_idx] + sorted_arr[median_idx-1]) / 2
        print(sorted_arr, median, median_idx)

if __name__ == "__main__":
    arr = [2, 1, 5, 0, 7, 2, 0, 5]
    running_median(arr)
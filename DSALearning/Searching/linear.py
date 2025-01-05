def linear_search(arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return i
    return "Element not found"
    
if __name__ == "__main__":
    print(linear_search([34,55,76,23,5,7], 5))
    print(linear_search([34,55,76,23,5,7], 0))
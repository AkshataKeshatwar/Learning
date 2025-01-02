def linearSearch(arr: list ,s:int) -> int:
    for i, a in enumerate(arr):
        if a == s:
            return i
    return -1


index = linearSearch([2,4,5,6,7,18,23,22,14], 5)
print(index)
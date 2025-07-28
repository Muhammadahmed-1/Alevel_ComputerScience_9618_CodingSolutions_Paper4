import random

ArrayData = [[0]*10 for i in range(10)]
for x in range(0, 10):
    for y in range(0, 10):
        ArrayData[x][y] = random.randint(1, 100)


def display(ArrayData):
    for x in range(0, 10):
        for y in range(0, 10):
            print(ArrayData[x][y], " ", end='')
        print("")


print("Before")
display(ArrayData)

arrayLength = 10
for x in range(arrayLength):
    for y in range(arrayLength - 1):
        for z in range(arrayLength - y - 1):
            if ArrayData[x][z] > ArrayData[x][z+1]:
                temp = ArrayData[x][z]
                ArrayData[x][z] = ArrayData[x][z+1]
                ArrayData[x][z+1] = temp

print("After")
display(ArrayData)


def recursiveBinarySearch(SearchArray, lower, upper, SearchVal):
    if upper >= lower:
        mid = (upper + lower) // 2
        if SearchArray[0][mid] == SearchVal:
            return mid
        elif SearchArray[0][mid] > SearchVal:
            return recursiveBinarySearch(SearchArray, lower, mid - 1, SearchVal)
        else:
            return recursiveBinarySearch(SearchArray, mid + 1, upper, SearchVal)
    return -1


# Example usage of recursiveBinarySearch
SearchVal = 42
result = recursiveBinarySearch(ArrayData, 0, 9, SearchVal)
if result != -1:
    print("Element", SearchVal, "found at index", result)
else:
    print("Element", SearchVal, "not found in the array.")

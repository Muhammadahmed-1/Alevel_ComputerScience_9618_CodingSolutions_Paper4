def recursiveBinarySearch(dataArray, lowerbound, upperbound, searchValue):
    if upperbound < lowerbound:
        return -1
    else:
        mid = lowerbound + (upperbound - lowerbound) // 2
        if dataArray[mid] < searchValue:
            return recursiveBinarySearch(dataArray, mid + 1, upperbound, searchValue)
        elif dataArray[mid] > searchValue:
            return recursiveBinarySearch(dataArray, lowerbound, mid - 1, searchValue)
        else:
            return mid

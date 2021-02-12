def BinarySearch(arr,key):
    high = len(arr) - 1
    low = 0
    middle= 0
  
    while low <= high: 
  
        middle = (high + low) 
        if arr[middle] < key: 
            low = middle + 1
        elif arr[middle] > key: 
            high = middle - 1
        else: 
            return middle
    return -1
print(BinarySearch([4,8,15,16,23,42],15))
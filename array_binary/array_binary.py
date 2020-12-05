# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):

    # Check base cases
    if  isinstance(x, str):
         return -2
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


def call_function(arr,x):

 result = binary_search(arr, 0, len(arr)-1, x)

 if result == -1:
      print("Element is not present in array")
 elif result == -2:
      print("Error!, just allowed to  enter an int value")
 else:
      print("Element is present at index", str(result))

arr = [ 2, 3, 4,8, 10, 40,60]
x = 4
call_function(arr,x)

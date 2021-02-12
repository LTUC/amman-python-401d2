def merge_sort(arr):
    n = len(arr)
    
    if n > 1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge_left_and_right(left, right, arr)

    print(arr)
    return arr

def merge_left_and_right(left, right, arr):
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    

arr = [9,78,5]
merge_sort(arr)
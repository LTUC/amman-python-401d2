def reverse_array(arr):
    """Reverses a list
    Args:
        arr (list): python list
    Returns:
        [list]: list in reversed form
    """
    # put your function implementation here
    array = []
    for x in range(len(arr)-1, -1, -1):
        array.append(arr[x])
    return array
print(reverse_array([1, 2, 3, 4, 5, 6]))
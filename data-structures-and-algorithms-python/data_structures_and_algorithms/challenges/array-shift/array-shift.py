import math
def shiftArray(arr, val):
    s = (len(arr)/2)
    d = math.ceil(s)
    print(arr[:d] + [val] + arr[d:])
    return(arr[:d] + [val] + arr[d:])

print('This is my birthDay and birthMonth and i wanna add 19 to complete the year')
shiftArray([1, 4, 6, 9, 8], 19)
print('DONE 🎉')
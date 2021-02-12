
def BinarySearch(arr,low,high,x):

    try:
        if type(x)!= int or x=="":
            print(f"Please insert integer \n ,{x} Not allowed to use or leave it empty")
        try:
            if high>= low:
                mid=(high+low)//2
                if arr[mid]==x:
                    return mid
                elif arr[mid]>x:
                    return BinarySearch(arr,low,mid-1,x)
                elif  x > arr[high]:
                    return -1
                else:
                    return BinarySearch(arr,low,mid+1,x)
            else:
                return -1
        except Exception as error:
            print(f"THE ERROR HAPPEND IS number greater than items of array : {error}")
    except Exception as error:
        print(f"THE ERROR HAPPEND IS validtion: {error}")


def fun_call(arr,x):
   
    try:
        result = BinarySearch(arr, 0, len(arr)-1, x)

        if result  >= 0:
            print("Element at index = ", str(result))
        elif  result <0 or result ==-1 or x> max(arr):
            print("Element is not in array",f" {str(result)}")
        else:
            print("Element is not in array",f" {str(result)}")
    except Exception as error:
        print(f"THE ERROR HAPPEND IS here : {error}")

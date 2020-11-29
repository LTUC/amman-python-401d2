def reverse_array():

 # put your function implementation here
 list = []
 n = int(input("Enter number of elements : "))
 for i in range(0, n):
    element = int(input())
    list.append(element) # adding the element

 list = list[::-1]
 print(list)

reverse_array()

def reverse_array_(arr):

# put your function implementation here

   arr.reverse()
   return arr


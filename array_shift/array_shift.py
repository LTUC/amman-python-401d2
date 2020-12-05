import math
def insertShiftArray(alist,variable):
  a=alist[:: ]
  length=len(a)
  m=math.ceil(length/2)
  a1=alist[0:m]
  v=[variable]
  a2=alist[m:length]
  return (a1+v+a2)


print(insertShiftArray([2,4,6,8],5))
print(insertShiftArray([4,8,15,23,42], 16))



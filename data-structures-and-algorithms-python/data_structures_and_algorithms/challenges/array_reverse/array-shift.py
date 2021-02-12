def insertShiftArray(alist,variable):
  a=alist[::]
  b=variable
  c=[]
  d=[]
  e=[b]
  for i in range(len(a)):
    if a[i]>b  :
        c.append(a[i])
    elif a[i]<b:
        d.append(a[i])
  return(d+e+c)



print(insertShiftArray([2,4,6,8],5))
print(insertShiftArray([4,8,15,23,42], 16))

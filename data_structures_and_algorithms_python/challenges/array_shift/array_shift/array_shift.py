a = [2,4,6,8]
idx = 2
value=[5]

def insertShiftArray(a,idx,value):
 b=a[:idx] + value + a[idx:]
 return b
print(insertShiftArray(a,idx,value))


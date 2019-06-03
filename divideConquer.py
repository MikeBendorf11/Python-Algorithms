import math

def countInst(arr, lft, rgt, val):
  if lft==rgt:
    if arr[lft] == val: 
      return 1
    else:
      return 0
  else:
    lCount = countInst(arr, lft, math.floor((lft+rgt)/2), val)
    rCount = countInst(arr, math.floor((lft+rgt)/2)+1, rgt, val)
    return lCount + rCount

def minMax(arr, lft, rgt, min, max):
  if lft==rgt:
    if arr[lft] > max:
      max = arr[lft]
    if arr[lft] < min:
      min = arr[lft]
    return (min,max)
  else:
    (min,max) = minMax(arr, lft, math.floor((lft+rgt)/2), min, max)
    (min,max) = minMax(arr, math.floor((lft+rgt)/2)+1, rgt, min, max)
    return (min,max)
    
#arr = [5,4,3,6,7,3,2,0]
print(minMax([4,1,9,0,4,4], 0, 5, 10, -10))




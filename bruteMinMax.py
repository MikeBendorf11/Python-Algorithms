def minMax(arr):
  min = arr[0]
  max = arr[1]
  for i in range(2,len(arr)):
    if(arr[i]<min):
      min = arr[i]
    if(arr[i]>max):
      max = arr[i]
  return (min, max)

print(minMax([5,6,4,3,67,5,0]))
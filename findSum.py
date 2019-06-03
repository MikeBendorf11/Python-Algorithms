#finds the sum of 2 numbers in an array that equal param 2
count = 0
def findSum(arr,x):
  for n in range(count+1, arr):
    if x == arr[count] + arr[n]:
      return (arr[count], arr[n])
    if count < range(arr):
      count += 1
      findSum(arr[count:range(arr)],x)


def findSum2(arr,x, size, result):
  if size>2:
    result = findSum2(arr[1:], x, size-1, result)
  for n in range(len(arr)-1):
    if x == arr[0] + arr[n+1]:
      result = [arr[0], arr[n+1]]
  return result

def findSum1(arr,x):
  return findSum2(arr, x, len(arr), [])
  
  

print(findSum1([1,2,3,8,9,4,0], 8))

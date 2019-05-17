def josephus(arr):
  while len(arr)>1:
    arr.pop(1)
    temp = arr[0]
    arr.pop(0)
    arr.append(temp)
    print(arr)

josephus([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])  
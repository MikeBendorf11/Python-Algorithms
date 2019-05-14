import numpy as np

def bubble_sort(list):
    sorted_list = list[:]
    is_sorted = False
    while is_sorted == False:
        swaps = 0
        for i in range(len(list) - 1):
          if sorted_list[i] > sorted_list[i + 1]: # swap
              temp = sorted_list[i]
              sorted_list[i] = sorted_list[i + 1]
              sorted_list[i + 1] = temp
              swaps += 1
              print(swaps)
          if swaps == 0:
            is_sorted = True
    return sorted_list

#selection sort
def SelectionSort(str):
  strList = list(str)
  for i in range(len(strList)-1) :
    min = i
    for j in range(i+1, len(strList)):
      if strList[j] < strList[min]:
        min = j
      temp = strList[i] 
      strList[i] = strList[min]
      strList[min] = temp
  return strList

#bubblesort
def BubbleSort(str):
  strList = list(str)
  for i in range(len(strList)-1):
    for j in range(len(strList)-1-i):
      if strList[j+1]<strList[j]:
        temp = strList[j]
        strList[j] = strList[j+1]
        strList[j+1] = temp
  return strList

#GroupColors
def GroupColors(arr):
  result = []
  for i in range(len(arr)):
    if arr[i] == 1:
      result.append(arr[i])
    else: 
      result.insert(0, arr[i])
  return result

# consider 0 is white and 1 is black
def MoveColors(arr):
  ordered = False
  lapse = 1
  arrIdeal = [0,0,0,0,1,1,1,1] 
  while ordered == False : 
    for i in range(len(arr)-1):
      if arr[i]>arr[i+1]:
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
        lapse +=1
    ordered = True if arr == arrIdeal else False
  print(lapse)    
  return(arr)

T = True
F = False
def Topology(node, length):
  tempMtx = [ [0 for x in range( length )] for y in range( length ) ]  
  for i in range(length)  :
    for j in range(length):
      if j == node and i!=j:
        tempMtx[i][j] = T
      else: 
        tempMtx[i][j] = F
    if node == length-1:
      node = 0
    else : 
      node += 1
  print(np.matrix(tempMtx))


#print(MoveColors([1,0,1,0,1,0,1,0]))
Topology(2, 4)
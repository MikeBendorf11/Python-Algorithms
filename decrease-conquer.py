import numpy as np
import cmath as math
print('hi')
#def binary_count(initial, objective):
  #digits = len(initial)

#a pattern generator for counting 2^3 by changing one digit at a time. Something like grey code, only that grey code works for 2^n not only 2^3

list = [-1,-2,-4]
laps = pow(2,len(list))-1
# counter = 0
# for i in range(laps):
#   while counter < len(list):
#     print(counter)
#     list[counter]*=-1
#     #print(list)
#     counter+=1
    
#   counter-=1
#   while counter > -1:
#     print(counter)
#     list[counter]*=-1
#     #print(list)
#     counter-=1
#   counter+=1

i=0
def mult(list):
  total = 0
  for val in list:
    if val>0:
      total +=val
  return total

arr = []
while(laps>0):
  
  for i in range(len(list)):
    laps-=1
    list[i]*=-1
    print(list) 
    arr.append(mult(list)) 
    #print(i)
  for i in range(len(list)-2,0,-1):
    laps-=1
    list[i]*=-1
    print(list)
    arr.append(mult(list))
    #print(i)

arr.sort()
print(arr)


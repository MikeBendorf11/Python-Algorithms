import cProfile
import numpy as np

arr = np.random.randint(500,size=500)
arr2 = []
for i in range(500, 0, -1):
  arr2.append(i)


def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot  
    for j in range(low , high): 
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i]  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
        i = j = k = 0         
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1        
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  
def heapify(arr, n, i): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2  
    if l < n and arr[i] < arr[l]: 
        largest = l 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
        heapify(arr, n, largest) 
  
def heapSort(arr): 
    n = len(arr) 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0) 

print('************************ quickSort ************************')
cProfile.run('quickSort(arr, 0 , len(arr)-1)')
print('************************mergeSort************************')
cProfile.run('mergeSort(arr)')
print('************************heapSort************************')
cProfile.run('heapSort(arr)')
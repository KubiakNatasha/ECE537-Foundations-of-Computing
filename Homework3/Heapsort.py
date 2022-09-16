from itertools import permutations
import time
from tkinter import N
import numpy as np
from math import e
 
#swaps performed by the procedure BUILD-MAX-HEAP and the number of swaps performed by the rest of the HEAPSORT

def HeapifyBUILD(arr,n,i):              #Function to count Heapify Counter 
    largest = i
    global BuildSwap                    #global Var
    L = i*2+1                           #left
    R = i*2+2                           #right

    if L < n and arr[L] > arr[largest]:
        largest=L
        
    if R < n and arr[R] > arr[largest] :
        largest=R
        
    if largest != i: 
        BuildSwap += 1          #Count Swaps
        t = arr[largest]
        arr[largest] = arr[i]
        arr[i] = t
        HeapifyBUILD(arr,n,largest) 
        
    return BuildSwap




def HeapifyHEAP(arr,n,i):               #Seperate function to count the Heapify Function Counter
    largest = i                         
    global HeapSwap
    L = i*2+1                           #left
    R = i*2+2                           #Right

    if L < n and arr[L] > arr[largest]:
        largest=L
        
    if R < n and arr[R] > arr[largest] :
        largest=R
        
    if largest != i: 
        HeapSwap += 1           #Count Swaps
        t = arr[largest]
        arr[largest] = arr[i]
        arr[i] = t
        HeapifyHEAP(arr,n,largest) 
    return HeapSwap


def BuildMaxHeap(arr,i):                                                                                
    s = i//2 - 1                                                       
    for x in range(s + 1):                                       
        HeapifyBUILD(arr,i,s-x)                                     
        # print("BuildMaxHeap Steps: ",arr)             #Commented out for time purposes
        
 

def HeapSort(arr,i):
    global HeapSwap
    BuildMaxHeap(arr,i)
    for x in range(i):
        t = arr[0]
        arr[0] = arr[i-x-1]
        HeapSwap += 1           #Count Swaps
        arr[i-x-1] = t
        HeapifyHEAP(arr,i-x-1,0)



Array = list(range(1, 21))
i=len(Array) 
HeapSwap = 0
BuildSwap = 0
for x in range(2000):
    RandomArray = np.random.permutation(Array)       
    HeapSort(RandomArray,i)
# print("Heapsort Final: ",RandomArray)     #Commented out for time purposes

####-------------------RESULTS------------------##
Si = BuildSwap/2000
Wi = HeapSwap/2000
print("------------------------------")
print("BuildMaxHeap TotalSwaps:",BuildSwap)
print("HEAPSORT Total Swaps:",HeapSwap)
print("------------------------------")
print("Si:",Si)
print("Wi:",Wi)
print("------------------------------")
print("Can observe there are more swaps occuring during HEAPSORT")
print("This is because HEAPSORT swaps within the Heapsort function")
print("where is swaps A[1] with A[i], and it also calls the Heapify Fucntion ")
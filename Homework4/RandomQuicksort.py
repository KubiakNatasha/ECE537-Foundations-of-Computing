# Natasha Kubiak
# Homework 4

import random

#-------------------------------------------------------------------------#
def Quicksort(A, p, r):
    if(p < r):
        q = RandomPivot(A, p, r)
        #print(q)                   #checking pivot IS random
        Quicksort(A , p , q-1)
        Quicksort(A, q + 1, r)
#-------------------------------------------------------------------------#
  
def RandomPivot(A , p, r):

    pivot = random.randrange(p, r)          #Choose Random Pivot from Range of Array
    A[p], A[pivot] = A[pivot], A[p]
    return RandomPartition(A, p, r) 
#-------------------------------------------------------------------------#
  
def RandomPartition(A,p,r):
    global Comparisons      #Count each comprison
    pivot = p 
    i = p + 1 
    for j in range(p + 1, r + 1):
        if A[j] <= A[pivot]:            #if A[j] is less than pivot
            A[i] , A[j] = A[j] , A[i]   #exchnage A[i] and A[j]
            Comparisons +=1 
            i = i + 1
    A[pivot] , A[i - 1] = A[i - 1] , A[pivot]   
    pivot = i - 1
    return (pivot)
  
#--------------------------------MAIN--------------------------------------#
Array = [5, 8, 17, 3, 14, 20, 18, 19, 10, 9, 7, 6, 15,11, 4, 1, 16, 2, 13, 12 ]
Comparisons = 0
Quicksort(Array, 0, len(Array) - 1)
print("Total Comparisons:", Comparisons)
# print(Array)
#---------Get average Comparisons-------------#
for x in range(1000):
    Comparison = 0
    Quicksort(Array, 0, len(Array) - 1)

Average = Comparisons/1000
#---------------------------------------------#
print("Comparison Average over 1000 iterations: ",Average)
print("Upper Bound Given in Book: 57 ")
print("Compared with O(nlgn) Average : 26")
print()
print("We can observe we are getting about the average case when")
print("we compare over 1000 iterations, otherwise the value ranges from 20-50")
print("which is expected as we would rarely reach the upper bound")
print()
  

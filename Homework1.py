from itertools import permutations
import time
from tkinter import N

n = 8
Array = [1,2,3,4,5,6,7,8]
print("The array is")
print(Array)
time.sleep(2)

#Python Function that will list each permutation of the Array
p = list(permutations(Array))

# for list in p:
#     print(list)

# print("starting analysis")
# time.sleep(2)




for x in p:                     # This gets every rand permutation of 8!
    best = 0  
    hire = 0                  # starting candidate is always hired 
    print(x)
    
    for i in x:                 # Next we will grab each individual potential hire in the list
        print(i)                # Just for checking visually
        if i > best:            # If candidate is better than the Hired person
            best = i            # Hire candidate
            print("Hire!!")
            hire = hire + 1
            # print("hire=", hire)
    print("hire=", hire)

            
            
    

n = 8;
   

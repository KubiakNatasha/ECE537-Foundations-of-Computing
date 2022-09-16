from itertools import permutations
import time
from tkinter import N
import numpy as np
from math import e



def Factorial():
    n = 8
    fact = 1
    
    for i in range(1,n+1):
        fact = fact * i

    return(fact)


Array = [1,2,3,4,5,6,7,8]
fact = Factorial()
ln8 = np.log(8)                 # assign the numpy log function to a new function called ln
hire = 0                        # End count of Hires per permutation
p = list(permutations(Array))   #Python Function that will create all permutation of the Array



for x in p:                     # This gets every rand permutation of Array[1....8]
    best = 0                    # starting candidate is always hired
    # print(x)                    # Just for checking visually
    for i in x:                 # Next we will grab each individual potential hire in the list
        # print(i)                # Just for checking visually
        if i > best:            # If candidate is better than the Hired person
            best = i            # Hire candidate
            # print("Hire!!")     # Just for checking visually
            hire = hire + 1     #Each time a HIRE occurs, add this to end count H1 + H2 +...Hn
            # print("hire=", hire)




print(" ")
print("Total Hires: ", hire)   
print(" ")




############# CALCULATIONS ###############

Expected = hire/fact            #theoretical expected value as EH = 1/8!(H1 + H2 + ... + H8!)
Harmonic= 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/7 + 1/8
# Variance = Summation(n) of (1/i)  - Summation(n) of (1/i^2)
Variance = (Harmonic) - pow(Harmonic,2)

################ PRINT OUT STATEMENTS ################
print("-----EXPECTATION-----")
print("Theoretical Expected Value:", Expected)
print("Value discussed in class as nth value Harmonic: ", Harmonic)
print("Value compared with ln(8): ", ln8)
print(" ")
print("------VARIANCE------")
print("Theoretical Variance:", Variance)



     

            
            
    


   

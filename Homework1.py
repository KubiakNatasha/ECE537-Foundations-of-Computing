from itertools import permutations
import time
from tkinter import N


def Factorial():
    n = 8
    fact = 1
    
    for i in range(1,n+1):
        fact = fact * i

    return(fact)


Array = [1,2,3,4,5,6,7,8]
fact = Factorial()
hire = 0                    # End count of Hires per permutation
#Python Function that will create all permutation of the Array
p = list(permutations(Array))



for x in p:                     # This gets every rand permutation of Array[1....8]
    best = 0                    # starting candidate is always hired
    # print(x)                  # Just for checking visually
    for i in x:                 # Next we will grab each individual potential hire in the list
        # print(i)                # Just for checking visually
        if i > best:            # If candidate is better than the Hired person
            best = i            # Hire candidate
            # print("Hire!!")   # Just for checking visually
            hire = hire + 1     #Each time a HIRE occurs, add this to end count H1 + H2 +...Hn
            # print("hire=", hire)





print("Total Hires: ", hire)   




############# CALCULATIONS ###############

Expected = hire/fact            #theoretical expected value as EH = 1/8!(H1 + H2 + ... + H8!)
#Var(H) = E(H^2) - (EH)^2 = 1/8!(H1^2 + H2^2 + ... + H81^2) - (EH)^2.
print("Theoretical Expected Value:", Expected)
print("Theoretical Variance:")



     

            
            
    


   

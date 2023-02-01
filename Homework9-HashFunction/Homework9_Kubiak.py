# Natasha Kubiak
# Homework 9
#-- Consider the hash function
#-- h(k, i) = (k + i (1 + k mod 16)) mod 17.
#-- Write a program to generate 16 random 3-digit integers and hash them into a 17-long hash table using h(k,i) above.
#-- Let X = the number of probes (i. e., the value of i in h(k,i) ) for the 5-th hashed integer; 
#-- let Y = the number of probes for the 16-th hashed integer; select at random one of the 16 hashed integers and 
#-- let Z be the number of its probes (i.e.: the probes used to hash it) .
#-- Repeat the experiment 100 times and get X_i, Y_i, Z_i for 1 <= i <= 100. 
#-- Output XX = 1/100 Sum_i X_i, YY = 1/100 Sum_i Y_i, ZZ = 1/100 Sum_i Z_i.
#-- In your report, in addition to giving the values XX, YY and ZZ, write a few sentences 
#-- comparing these values with the theoretical bounds given in the lectures.

from asyncio.windows_events import NULL
import random
import numpy as np


global X                                          # X = the number of probes (i) for the 5-th hashed integer
global Y                                          # Y = the number of probes for the 16-th hashed integer
global Z                                          # Z = number of probes for random int

X = 0
Y = 0
Z = 0
lists = [[] for i in range(17)]                 # Create 17 Lists, all set to 0 so we can check if
index = list(range(0, 16, 1))
# print(lists)                                     # there are collisions or not later

for t in range(100):
    for i in index:                            # Create 16 Random Numbers
        num = random.randrange(100, 1000, 1)        # Range 100 -> 999, incriments of 1

        while lists is []:
            h = ((num + 0 )*(1 + (num % 16)))%17
            #print(index)
            if (index[i] == 4):
                    X += 1

            if (index[i] == 15):
                    Y += 1
                
            if (index[i] == random.randrange(0, 16, 1)):
                    Z +=  1

                    #------check until bucket is empty--------#
                    if not lists[probe_hash]:                           # if EMPTY
                                lists[probe_hash] = num                 # enter num
                                break                                   # repeat until empty bucket, increasing probe
        
print("XX = 1/100 * Sum_i X_i where X_i =", X)    
print("XX = ", X/100)  
print("-------------------")
#----------------------------------------------#
print("YY = 1/100 * Sum_i Y_i where Y_i =", Y)  
print("YY = ", Y/100)  
print("-------------------")
#------------------------------------------------#
print("ZZ = 1/100 * Sum_i Z_i where Z_i =", Z)  
print("ZZ = ", Z/100)   
print("-------------------")
print("Theoretical Bound from Lecture:")
print("Upper bound on expected number of probes to insert an element into table size (m) with (n) elements already hashed:")
print("1/(1-(alpha)) , where alpha = m/n and m = 17")
print("5th = 1/(1-(n/m) = ", 1/(1-(5/17)))
print("16th = 1/(1-(n/m) = ", 1/(1-(16/17)))
print("Lower bound = 1/alpha * ln(1/1-alpha")
print("5th = 1/(1-(n/m) = ", 1/(5/17)* np.log(1/(1-(5/17))))
print("16th = 1/(1-(n/m) = ", 1/(16/17)* np.log(1/(1-(16/17))))

print("note: I could not figure out to count the probes accurately, but based on the theoretical")
print("results, this seems to be what I expected")


            
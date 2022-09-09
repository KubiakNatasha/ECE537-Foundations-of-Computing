from itertools import permutations
import time
from tkinter import N
import numpy as np
from math import e

    #                       np.random.permutation()
    # This is what creates a random permutation of the numbers 1-8 in an array
    # Randomly permute a sequence, or return a permuted range.
    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.permutation.html?

#------------------------------------------------------------------------------------------------------#
def nthHarmonic(N) :
    # Function for nth Value Harmonic...
    harmonic = 1
    for i in range(2, N + 1) :
        harmonic += 1 / i
    return harmonic
#------------------------------------------------------------------------------------------------------#

def Random8():
    Array = [1,2,3,4,5,6,7,8]
    hire = 0                        # End count of Hires per permutation

    for x in range(1000):                                         # Run 1,0000 times
        best = 0       
        RandomArray = np.random.permutation(Array)              # starting candidate is always hired
        #print(RandomArray)                                      # Just for checking visually
        for i in RandomArray:                                             # Next we will grab each individual potential hire in the list
            # print(i)                                          # Just for checking visually
            if i > best:                                        # If candidate is better than the Hired person
                best = i                                        # Hire candidate
                # print("Hire!!")                               # Just for checking visually
                hire = hire + 1                                 #Each time a HIRE occurs, add this to end count H1 + H2 +...Hn
                # print("hire=", hire)

    ############# CALCULATIONS ###############
    SampleMean = hire/1000           
    ################ PRINT OUT STATEMENTS ################
    print("----- RANDOM HIRING FOR 8 COMPARISON -----")
    print("----------------------")
    print("| Total Hires: ", hire,"|")   
    print("----------------------")
    print("Sample Mean:", SampleMean)
    print("Theoretical Expectation found in HW1: 2.7178")
    print(" ")

def Random20():
    Array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
    N = 20               
    hire = 0                        # End count of Hires per permutation

    for x in range(1000):                                         # Run 1,0000 times
        best = 0       
        RandomArray = np.random.permutation(Array)              # starting candidate is always hired
        #print(RandomArray)                                     # Just for checking visually
        for i in RandomArray:                                   # Next we will grab each individual potential hire in the list
            # print(i)                                          # Just for checking visually
            if i > best:                                        # If candidate is better than the Hired person
                best = i                                        # Hire candidate
                # print("Hire!!")                               # Just for checking visually
                hire = hire + 1                                 #Each time a HIRE occurs, add this to end count H1 + H2 +...Hn
                # print("hire=", hire)

    ############# CALCULATIONS ###############
    SampleMean = hire/1000       
    Theoretic = nthHarmonic(N)
    ################ PRINT OUT STATEMENTS ################
    print("----- RANDOM HIRING FOR 20 COMPARISON -----")
    print("----------------------")
    print("| Total Hires: ", hire,"|")   
    print("----------------------")
    print("Sample Mean:", SampleMean)
    print("Theoretical Expectation:",Theoretic)
    print(" ")


#----------------------------START OF PROGRAM--------------------------------#
Random8()
Random20()


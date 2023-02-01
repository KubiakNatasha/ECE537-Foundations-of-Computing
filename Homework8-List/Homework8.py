# Natasha Kubiak
# Homework 8
#-- Write a program that generates randomly one hundred 3-digit integer numbers
#-- and stores them in 10 lists according to their least significant digit, 
#-- while keeping track of the order in which they were stored.  
#-- Then select randomly one of the 100 numbers you generated, call it i, 
#-- and check the number N(i) of  integers that were inserted in i's list AFTER i.
#-- Repeat the experiment above 100 times and get Ñ = 1/100 Sum_i N(i).

import random

                                #-------PART 1--------#
                        # create 100 rand num and store in 10 lists #
                                                
lists = [[] for i in range(10)]                 # Create 10 Lists
Sum = 0                                         # Summation

for x in range(100):                            # Create 100 Random Numbers
    num = random.randrange(100, 1000, 1)        # Range 100 -> 999, incriments of 1
    #print(num)
    LSB = num % 10                              # use MOD to get the LSB
    #print(LSB)
    lists[LSB].append(num)                      #numbers will be added to list based on LSB

# Checking that insertion into the lists worked as expected
print("--Lists--")
print("")
print("0: ",lists[0])
print("1: ",lists[1])
print("2: ",lists[2])
print("3: ",lists[3])
print("4: ",lists[4])
print("5: ",lists[5])
print("6: ",lists[6])
print("7: ",lists[7])
print("8: ",lists[8])
print("9: ",lists[9])



                                #-------PART 2--------#
            # randomly select a number out of the 100, check how many numbers were inserted after

for i in range(100):                                              # RUN EXPIRIMENT 100 TIMES

    RandList = random.randrange(0, 10)                          # randomly select from 0-9 lists
    #print("List",RandList)
    Ni = random.choice(lists[RandList])                         # From that list, grab a random number
    #print("Number",Ni)                                                   
    position = lists[RandList].index(Ni)                        # Grab position of Ni in the list, using python index(value) 
    #print("Position",position)
    length = len(lists[RandList])                               # Grab length of List
    value = length - (position+1)                               # since we index at 0, we add 1 to the position
    #print("Length of array",length)
    #print("Value",value)
    Sum += value                                              #iterate to add to the Summation

print("The Summation over 100 Expiriments is: ",Sum)

N = Sum / 100
print("The average is: ", N)

print("")
print("--Notes--")
print("We observe the Average is around ranges from 4.0 to 5.0 values that occur after our random value Ni")
print("on average each list will get around 10 values in each list out of 100")
print("randomly selecting a value in each list will give about 4.5-5( or HALF of the list) values after the randomly selected one")
print("I agree with this result as it makes sense given the amount of values and lists and how they are")
print("randomly distribiuted on average")
  



      
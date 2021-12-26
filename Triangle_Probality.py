'''You have a stick of arbitrary length. You break the stick uniformly at random along it’s length at two places, leaving you with three distinct pieces.
What is the probability that you can form a triangle with the resulting three pieces?'''

import random                                                       #To generate Random Numbers
triangle=0                                  
length=2
for i in range(10000):                                              #We are doing this experiment for 10000 times
    a=round(random.uniform(0.00001, (length-0.00001)),5)            #Selecting radom number between 0.00005 to lenght.Here we are taking ver low value.Cause lenght is greater than 0
    b=round(random.uniform(0.00001,(length-0.00001)),5)             #Selecting another random point
    while a==b:                                                     #To make sure both point we selected are not same
        b=round(random.uniform(0.00001,(length-0.00001)),5)         
    l1=round(min(a,b),5)                                            #Calculating first length
    l2=round(abs(a-b),5)                                            #Calculating second length
    l3=round(length-(l1+l2),5)                                      #Finally the third length
    max_lenght=max(l1,l2,l3)                                        #Determing the longest length
    if max_lenght<(length-max_lenght):                              #Triangle Inequality to check if given lenghts satisfy the codition
        triangle=triangle+1
print(triangle/i)                                                   #Finally the probality [(total favourable cases) /(total experiments)]

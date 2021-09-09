#!/usr/bin/python

from random import randint
sequence=[]
for number in range (100):
   myNumber=randint(1,1000) #Inclusive
   print myNumber
   sequence.append(myNumber)
print "The biggest number in this sequence is:", max(sequence)
print "The smallest number in this sequence is:", min(sequence)
print "'\033[94m',Kathryne Zong"

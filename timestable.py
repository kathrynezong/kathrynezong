#!/usr/bin/python
from __future__ import division
import numpy as np

#this is times table
for number1 in range (20,30):
   for number2 in range (20,30):
      print number1,"*",number2,"=",number1*number2
  
#this is addition
for number1 in range (5,16):
   for number2 in range (5,16):
      print number1,"+",number2,"=",number1+number2

#this is subtraction
for number1 in range (5,16):
   for number2 in range (5,16):
      print number1,"-",number2,"=",number1-number2

#this is divison
for number1 in range (5,16):
   for number2 in range (5,16):
      print number1,"/",number2,"=",number1/number2
      #print number1

for starweird in range (1,30):
   print starweird*"*"

for i in range (1,30):
   print (16-i)*" ",i*"*"

print "4/5=",4/5

print "4+5=",4+5
print "5-4=",5-4

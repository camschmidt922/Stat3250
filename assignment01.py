# #
# # File: assignment01.py (STAT 3250)
# # Topic: Assignment 1 
# #
from itertools import product

# # Two *very* important rules that must be followed in order for your assignment
# # to be graded correctly:
# #
# # a) The file name must be exactly "assignment01.py" (without the quotes)
# # b) The variable names followed by "= None" must not be changed and these names
# #    variable names should not be used anywhere else in your file.  Do not  
# #    delete these variables, if you don't know how to find a value just leave 
# #    it as is. (If a variable is missing the autograder will not grade any of 
# #    your assignment.)

##  For each question use the following lists as needed:
list01 = [2,5,4,9,10,-3,5,5,3,-8,0,2,3,8,5,2,-3,8,7]
list02 = [-7,-3,8,-5,-5,2,4,9,10,-7,9,10,2,13,-12,-4,1,3,5]
list03 = [2,-5,6,0,7,-2,-3,5,0,2,8,7,9,2,0,-2,5,5,6]
list04 = [3,5,-10,2,0,4,-5,-7,6,2,3,3,5,12,-5,-9,-7,4]
biglist = list01 + list02 + list03 + list04

# # 1.  Find the product of the last five elements of list04.
temp1 = list04[-5:]
# Created a list with the last five elements of list04 using the colons and index to represent
# the fifth to last value to the end of the list
product = 1
# Created an object that would become the final project. Starts at 1 because when I multiply it
# with the first element of temp1, it will become that element.
for i in temp1:
    product *= i
# Multiplies each element with product, which creates an iterative process that multiples
# one times the first element times the second element and so forth
q1 = product


# # 2.  Extract the sublist of list01 that goes from
# #      the 4th to the 10th elements (inclusive).

# Created a subset of list01 using a sequence of every integer from 3 to 10, not including 10.
# This sequence is 3, 4, . . . 9. These are the indexes of elements 4 through 10 in list01.
q2 = list01[3:10]


# # 3.  Concatenate list01 and list04 (in that order), sort
# #      the combined list, then extract the sublist that 
# #      goes from the 6th to the 17th elements (inclusive).

temp2 = list01 + list04
temp2.sort()
# Created a new list in which I saved the concatenation of list01 and list04.
# The new list was then sorted and had a subset from indexes 5 to 16 inclusive taken,
# which corresponds to elements 6 to 17 inclusive.
q3 = temp2[5:17]


# # 4.  Generate "biglist", then extract the sublist of every 5th 
# #      element starting with the 4th list element

temp3 = []
# Created a new list that will become the sublist.
for i in range(3, len(biglist), 5):
    temp3.append(biglist[i])
# This for loop starts at 3 and counts by 5 until it reaches the length of bigList. I use
# the loop's index as an index for extracting values from bigList. It starts at the 4th element,
# which is indexed by 3, and then every 5th element from there. It appends each selected value
# to our new list, which becomes the desired sublist.
q4 = temp3


# # 5.  Determine the number of times that 3 appears in biglist.

# Using the count function on the list, which will return how many times the given parameter
# appears in the list.
q5 = biglist.count(3)



# # 6.  Determine the index for the first appearance of 12 in biglist.

# Using the index function, which returns the index of the first appearance of the given
# parameter in the list.
q6 = biglist.index(12)

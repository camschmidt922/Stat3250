##
## Assignment 00, STAT 3250
##

## This assignment is for practice only, the score will not be used.

## Two *very* important rules that must be followed in order for your assignment
## to be graded correctly:
##
## a) The file name must be exactly "assignment00.py" (without the quotes)
## b) The variable names followed by "= None" must not be changed and these names
##    should not be used anywhere else in your file.  Do not delete these 
##    variables, if you don't know how to find a value just leave it as is.
##    (If a variable is missing the autograder will not grade any of your
##    assignment.)

## When you answer each question, replace the "None" to the right of the equals
## sign with code or the correct value.

## Question 1
##
## Find the sum of 23 and 119

q1 = 23+119
## Using the basic math operations to find the given sum as 142. The solution appears in the
## console, but if you are running the code as a whole rather than line-by-line (at least on
## my IDE) you would need to print it out to see the solution with print(23+119).

## Question 2
##
## Create a list with "Hello" as the first element and "World" as the second element.

q2 = myList = ["Hello", "World"]
## Created a list called myList that contains two strings, as indicated by the quotation marks.


## Question 3

## Determine the first 5 prime numbers, in order.  Then give: 
##   (a) the largest of these 
##   (b) a list of the 1st, 2nd, and 4th of these (when small to large)
##   (c) a list of all 5 (smallest to largest)

# Building my list that will store prime numbers
primeList = []
# Now a function to determine if numbers are prime
def isPrime(n):
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# This while loop will fill primeList with prime numbers until it's length exceeds 4 (in other
# words, is equal to 5)
n=1
while len(primeList) < 5:
    if isPrime(n):
        primeList.append(n)
    n += 1

## 3(a)
# Taking index -1 from primeList, which gives the first item from the end
q3a = primeList[-1]

## 3(b)
# Building a new list using indexes 0 (first item), 1 (second item), and 3 (fourth item)
# from primeList
q3b = [primeList[0], primeList[1], primeList[3]]

## 3(c)
# primeList is already in order from how I selected the first 5 prime numbers
q3c = primeList

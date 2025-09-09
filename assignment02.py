# #
# # File: assignment02.py (STAT 3250)
# # Topic: Assignment 2
# #

# # Two *very* important rules that must be followed in order for your 
# # assignment to be graded correctly:
# #
# # a) The file name must be exactly "assignment02.py" (without the quotes)
# # b) The variable names followed by "= None" must not be changed and these 
# #    names variable names should not be used anywhere else in your file.  Do   
# #    not delete these variables, if you don't know how to find a value just  
# #    leave it as is. (If a variable is missing the autograder will not grade  
# #    any of your assignment.)


# # Questions 1-7: For the questions in this part, use the following
# #  lists as needed:

list01 = [5, -9, -1, 8, 0, -1, -2, -7, -1, 0, -1, 6, 7, -2, -1, -5]
list02 = [-2, -5, -2, 8, 7, -7, -11, 1, -1, 6, 6, -7, -9, 1, 5, -11]
list03 = [9, 0, -8, 3, 2, 9, 3, -4, 5, -9, -7, -3, -11, -6, -5, 1]
list04 = [-4, -6, 8, 8, -5, -5, -11, -3, -1, 7, 0, 2, -5, -2, 0, -5]
list05 = [-11, -3, 8, -9, 2, -8, -7, -12, 7, 3, 2, 0, 6, 4, -11, 6]
biglist = list01 + list02 + list03 + list04 + list05

# # Questions 1-7: Use for loops to answer each of the following applied  
# #  to the lists defined above.

# # 1.  Add up the squares of the entries of biglist.
total1 = 0
for i in biglist:
    total1 += i
# Defined a new variable, total, to be the sum of all the lists. It starts at 0,
# then for each element in bigList, it adds it to total.
q1 = total1   # sum of squares of entries of biglist

# # 2.  Create "newlist01", which has 14 entries, each the sum of the 
# #      corresponding entry from list01 added to the corresponding entry
# #      from list02.  That is,
# #     
# #         newlist01[i] = list01[i] + list02[i] 
# #
# #      for each 0 <= i <= 13.

newlist01 = []
for i in range(16):
    newlist01.append(list01[i]+list02[i])
# Created a new list called newlist01 and left it empty. Then, for every index of list01/list02,
# which ranges from 0-15 inclusive, I added an element into newlist01 that corresponded to adding
# that element of list01 and list02. I used range(16) since it would provide 0-16 noninclusive of the 16.
q2 = newlist01   # newlist01


# # 3.  Determine the number of entries in biglist that are less than 6.
count = 0
for i in biglist:
    if i < 6:
        count += 1
# Created a variable to count the number of entries that are less than 6, which starts at 0. Then, for all elements
# of biglist, if that element is less than 6, I add one to the count.
q3 = count   # number of entries in biglist less than 6


# # 4.  Create a new list called "newlist02" that contains the elements of
# #      biglist that are greater than 5, given in the same order as the
# #      elements appear in biglist.

newlist02 = []
for i in biglist:
    if i > 5:
        newlist02.append(i)
# Created a new, empty list. Then, for all elements of biglist, if they are greater than 5, I add
# them to newlist02.
q4 = newlist02   # newlist02


# # 5.  Find the sum of the positive entries of biglist.
total5 = 0
for i in biglist:
    if i >0:
        total5 += i
# Created a new variable called total5, and set it equal to 0 to represent the start of the sum. Then, for
# every element in biglist, if it is greater than 0 (positive), then I add it to total5, giving a sum of all
# positive elements.
q5 = total5   # sum of the positive entries of biglist


# # 6.  Make a list of the first 19 negative entries of biglist, given in
# #      the order that the values appear in biglist.
newlist03 = []
for i in biglist:
    if len(newlist03) < 19 and i < 0:
        newlist03.append(i)
# created a new, empty list. Then, for every element in biglist, if the length of the new list is less than 19 and
# that element is less than 0 (negative), I add that element to the new list. The check for the length of the new
# list is to restrict the number of elements added to 19.
q6 = newlist03   # list of first 19 negative entries of biglist


# #  7. Identify all elements of biglist that have a smaller element that 
# #      immediately precedes it.  Make a list of these elements given in
# #      the same order that the elements appear in biglist.
newlist04 = []
for i in range(1, len(biglist)):
    if biglist[i] > biglist[i-1]:
        newlist04.append(biglist[i])
# Created a new, empty list. Then, I created a for loop that indexed from 1 to the length of biglist, with the
# length of biglist not being included. Then I compared each element at the index to the element before. I started at
# index 1 because there is no element before index 0, so it would throw an error. Likewise, for this same reason,
# the first element cannot be in the new list. If the element at the index was greater than the one before it (a smaller
# element precedes it), then I add it to the new list.
q7 = newlist04   # list of elements preceded by smaller element


# # Questions 8-9: These questions use simulation to estimate probabilities and expected values.  

# #  8. Consider the following game: You flip a fair coin. If it comes up tails, then you win 1 dollar.
# If it comes up heads, then you win 1 dollar and get to simultaneously flip four more fair coins. In this case
# you win 1 dollar for each head that appears on the additional four flips, plus you get an extra 7 dollars if all five
# flips (the initial flip plus four additional flips) are heads.
# #      Use 100,000 simulations to estimate the average amount of money won when playing this game.
import numpy as np
# Importing NumPy in order to use its features.
def game(iterations):
    games = []
    for i in range(iterations):
        flips = [np.random.binomial(n=1, p=0.5)]
        if flips[0] == 1:
            for j in range(4):
                flips.append(np.random.binomial(n=1, p=0.5))
        money = int(np.sum(flips))
        if money == 5:
            money += 7
        games.append(money)
    return games
# Built a method that simulates the game for a given number of iterations. It first creates a list that will store game
# results. Then, it uses a for loop that will run the game the given number of iterations. Each run of this loop will
# create a list of flip results with heads being denoted by 1 and tails being denoted by 0. This list is created with
# the first coin flip included. Each coin flip is generated by using NumPy, creating a random binomial variable with
# n=1 and probability of .5. Using 1 for n renders this as a Bernoulli variable. Then I run a check to see if the
# result was heads. If it was, it runs another loop with 4 iterations, each adding an identical coin flip to the list.
# After all of this, the money value is assigned as the sum of all the results of flips (which now represents the
# number of heads that are flipped). If this number is not 5 (all 5 heads), it is fine as is. However, if it is 5, the
# bonus of 7 must be added, which is done by the conditional. It adds this final money value to the list of game
# results, which upon n iterations will grow to have length n. Then, I use the mean function in NumPy to assign the
# mean of this list with 100000 iterations (and thus the average earnings of 100000 iterations of the game) to q8.

q8 = np.mean(game(100000))  # mean winnings from 100,000 times playing the game

# #  9. Jay is taking a 15 question true/false quiz online. The
# #      quiz is configured to tell him whether he gets a question
# #      correct before proceeding to the next question.  The 
# #      responses influence Jay's confidence level and hence his 
# #      exam performance.  In this problem we will use simulation
# #      to estimate Jay's average score based on a simple model.
# #      We make the following assumptions:
# #    
# #      * At the start of the quiz there is a 81% chance that 
# #        Jay will answer the first question correctly.
# #      * For all questions after the first one, if Jay got 
# #        the previous question correct, then there is a
# #        90% chance that he will get the next question
# #        correct.  (And a 10% chance he gets it wrong.)
# #      * For all questions after the first one, if Jay got
# #        the previous question wrong, then there is a
# #        72% chance that he will get the next question
# #        correct.  (And a 28% chance he gets it wrong.)
# #      * Each correct answer is worth 5 points, incorrect = 0.
# #
# #      Use 100,000 simulated quizzes to estimate Jay's average 
# #      score.

q9 = None  # mean score from 100,000 simulated quizzes

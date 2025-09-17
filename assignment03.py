# #
# # File: assignment03.py (STAT 3250)
# # Topic: Assignment 3 
# #

# #  The questions in this assignment refer to the data in the
# #  file 'absent.csv'.  The data contains 740 records from an
# #  employer, with 21 columns of data for each record.  (There
# #  are a few missing values indicated by zeros where zeros 
# #  are clearly not appropriate.)  The file 'absent.pdf' has
# #  a summary of the meanings for the variables.
# #
# #  All of these questions can be completed without loops.  You 
# #  should try to do them this way, "code efficiency" will take 
# #  this into account.

import numpy as np  # load numpy as np
import pandas as pd # load pandas as pd

absent = pd.read_csv('absent.csv')  # import the data set as a pandas dataframe

# # 1.  Find the median absent time among all records.

q1 = np.median(absent["Absenteeism time in hours"])  # median of "Absenteeism" hours
# Subsetted the dataframe using brackets and the name of the column, then used the median function
# from numpy to get the median.

# # 2.  Determine the number of records corresponding to
# #     being absent on a Thursday.

q2 = np.sum(absent["Day of the week"]==5)
# Creates an array of logical values that represent whether the day of the week value of the absence is Thursday (5), then
# takes a sum of the array (True=1, False=2) to count it.


# # 3.  Find the number of unique employees IDs represented in 
# #     this data.  

q3 = len(absent["ID"].unique())  # number of unique employee IDs
# Used the unique function on the ID column of the absent data frame to get an array of just unique values, then
# got the length to get the total count.


# # 4.  Find the average transportation expense for the employee 
# #     with ID = 25.

q4 = np.mean(absent.loc[absent["ID"]==25, ["Transportation expense"]])  # Average transportation expense, ID = 25

# The conditional in creates a logical array that is used to subset the rows of the data frame (includes when true)
# that has every single occurrence when the ID is 25. The overall subset then only includes the information from
# the expense column, so it ends up being an array of expenses, which I use numpy to take the mean of.

# # 5.  Find the total number of hours absent for the records
# #     for employee ID = 20.

q5 = np.sum(absent.loc[absent["ID"]==20,"Absenteeism time in hours"])  # total hours absent, ID = 20
# Same process as the previous problem to get the subset, but this time I take data from the hours absent instead of
# transportation expenses. Then, I use sum to get the total.

# # 6.  Find (a) the median number of hours absent for the records of those who 
# #     have no pets, then (b) do the same for those who have at least two pets.

q6a = np.median(absent.loc[absent["Pet"]==0,["Absenteeism time in hours"]]) # median hours absent, no pet
q6b = np.median(absent.loc[absent["Pet"]>1,["Absenteeism time in hours"]]) # median hours absent, at least two pets
# Same process to get the subsets, just now conditioning based on pets and only grabbing the hours absent information.
# For the first part, setting number pets equal to 0, and for the second part, more than 1 pet is the same as at least
# two.


# # 7.  Among the records for absences that exceeded 7 hours, find (a) the 
# #     proportion that involved smokers.  Then (b) do the same for absences 
# #     of no more than 7 hours.

q7a = (np.sum(absent.loc[absent["Absenteeism time in hours"]>7, "Social smoker"])
       /len(absent.loc[absent["Absenteeism time in hours"]>7]))# proportion of smokers, absence greater than 7 hours
q7b = (np.sum(absent.loc[absent["Absenteeism time in hours"]<=7, "Social smoker"])
       /len(absent.loc[absent["Absenteeism time in hours"]<=7])) # proportion of smokers, absence no more than 7 hours
# The bottom term in both expressions is the subset of absences that meet the given time constraints. By taking the
# length of this array, you get the total number of absences that are of that time constraint. Then, for the top term,
# you only display the column of the same subset with the smoker data. Since this is 1 for true and 0 for false, you
# can just directly sum the column in order to get the count of the subset that involved a smoker.


# # 8.  Repeat Question 7, this time for social drinkers in place of smokers.

q8a = (np.sum(absent.loc[absent["Absenteeism time in hours"]>7, "Social drinker"])
       /len(absent.loc[absent["Absenteeism time in hours"]>7])) # proportion of social drinkers, absence greater than 7 hours
q8b = (np.sum(absent.loc[absent["Absenteeism time in hours"]<=7, "Social drinker"])
       /len(absent.loc[absent["Absenteeism time in hours"]<=7])) # proportion of social drinkers, absence no more than 7 hours
# Feel comments here are redundant.


# # 9.  Find the top-8 employee IDs in terms of total hours absent.  Give
# #     the IDs and corresponding total hours absent as a Series with ID
# #     for the index, sorted by the total hours absent from most to least.
# #     If there are ties for the 6th most absent employee, include all IDs that tie for 6th.

q9 = absent["Absenteeism time in hours"].groupby(absent["ID"]).sum().sort_values()[:8]  # Series of top-8 employee IDs in terms of total hours absent
# Groups a subset including only absenteeism time by ID number and then sums the total hours absent for each ID number.
# Then, it sorts this series and subsets by taking up to and including the 8th item of it.

# # 10. Find the median hours absent per record for each day of the week.
# #     Give the day number and median as a Series with the day number
# #     as the index, sorted by day number from smallest to largest.

q10 = None  # Series of median hours absent by day of week.


# # 11. Repeat Question 10 replacing day of the week with month.
# #     Give the month number and median as a Series with the month number
# #     as the index, sorted by month number from smallest to largest.

q11 = None  # Series of median hours absent by day of week.


# # 12. Find the top 4 most common reasons for absence for the social drinkers.
# #      Give the reason code and number of occurances as a Series with the 
# #      reason code as the index, sorted by number of occurances from
# #      largest to smallest.  (If there is a tie for 4th place,
# #      include all that tied for that position.)

q12 = None  # Series of reason codes and counts

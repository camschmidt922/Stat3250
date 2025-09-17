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

q2 = np.sum(absent["Day of the week"]==3)
# Creates an array of logical values that represent whether the day of the week value of the absence is Tuesday (3), then
# takes a sum of the array (True=1, False=2) to count it.


# # 3.  Find the number of unique employees IDs represented in 
# #     this data.  

q3 = len(absent["ID"].unique())  # number of unique employee IDs
# Used the unique function on the ID column of the absent data frame to get an array of just unique values, then
# got the length to get the total count.


# # 4.  Find the average transportation expense for the employee 
# #     with ID = 25.

q4 = np.mean(absent.loc[absent["ID"]==25, ["Transportation expense"]])  # Average transportation expense, ID = 25


# # 5.  Find the total number of hours absent for the records
# #     for employee ID = 20.

q5 = None  # total hours absent, ID = 20


# # 6.  Find (a) the median number of hours absent for the records of those who 
# #     have no pets, then (b) do the same for those who have at least two pets.

q6a = None # median hours absent, no pet
q6b = None # median hours absent, at least two pets


# # 7.  Among the records for absences that exceeded 7 hours, find (a) the 
# #     proportion that involved smokers.  Then (b) do the same for absences 
# #     of no more than 7 hours.

q7a = None # proportion of smokers, absence greater than 7 hours
q7b = None # proportion of smokers, absence no more than 7 hours


# # 8.  Repeat Question 7, this time for social drinkers in place of smokers.

q8a = None # proportion of social drinkers, absence greater than 7 hours
q8b = None # proportion of social drinkers, absence no more than 7 hours


# # 9.  Find the top-8 employee IDs in terms of total hours absent.  Give
# #     the IDs and corresponding total hours absent as a Series with ID
# #     for the index, sorted by the total hours absent from most to least.
# #     If there are ties for the 6th most absent employee, include all IDs that tie for 6th.

q9 = None  # Series of top-8 employee IDs in terms of total hours absent


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

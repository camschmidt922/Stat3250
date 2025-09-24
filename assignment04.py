# #
# # File: assignment04.py (STAT 3250)
# # Topic: Assignment 4 
# #
import numpy as np
# #  This assignment requires the data file 'diabetic_data.csv'.  This file
# #  contains records for over 100,000 hospitalizations for people who have
# #  diabetes.  The file 'diabetic_info.pdf' contains information on the
# #  codes used for a few of the entries.  Missing values are indicated by
# #  a '?'.  You should be able to read in this file using the usual 
# #  pandas methods.

# #  The Gradescope autograder will be evaluating your code on a reduced 
# #  version of the diabetic_data.csv data that includes about 35% of the
# #  records.  Your code needs to automatically handle all assignments
# #  to the variables q1, q2, ... to accommodate the reduced data set,
# #  so do not copy/paste things from the console window, and take care
# #  with hard-coding values. 

# #  Note: Many of the questions on this assignment can be done without the 
# #  use of loops, either explicitly or implicitly (apply). Scoring will take
# #  this into account.

import pandas as pd # load pandas as pd

dia = pd.read_csv('diabetic_data.csv')
dia1 = dia.loc[:10,:]

# # 1.  Determine the average number of procedures ('num_procedures') for 
# #     those classified as females and for those classified as males.

q1f = np.mean(dia.loc[dia["gender"]=="Female", "num_procedures"])  # female average number of procedures
q1m = np.mean(dia.loc[dia["gender"]=="Male", "num_procedures"])  # male average number of procedures
# Takes the mean of a subset of the dataset that is formed by taking the num_procedure column of any rows where
# the value in the gender row is the desired gender.

# # 2.  Determine the average length of hospital stay ('time_in_hospital')
# #     for each race classification.  (Omit those unknown '?' but include 
# #     those classified as 'Other'.)  Give your answer as a Series with
# #     race for the index sorted alphabetically.

q2 = dia.loc[dia["race"] != "?","time_in_hospital"].groupby(dia["race"]).mean().sort_index()# Series of average length of stay by race
# Uses the groupby function to create groups of a subset of the data that excludes rows where the race is unknown and
# only includes the value from the time_in_hospital column. It then takes the mean of each group and sorts by the index.

# # 3.  Determine the percentage of total days spent in the hospital due to
# #     stays ("time_in_hospital") of at least 5 days. (Do not include the %
# #     symbol in your answer.)

q3 = np.sum(dia.loc[dia["time_in_hospital"] >=5, "time_in_hospital"])/np.sum(dia.loc[:,"time_in_hospital"])*100  # percentage of days from stays of at least 5 days
# Sums the values in the time_in_hospital column for all rows where the value in that column is at least 5. Then, divides
# by the total of all values in the time_in_hospital column, and multiplies by 100 to get a percentage.

# # 4.  Among the patients in this data set, what percentage had at least
# #     four recorded hospital visits?  Each distinct record can be assumed 
# #     to be for a separate hospital visit. Do not include the % symbol in
# #     your answer.

q4 = len(dia.groupby(dia["patient_nbr"]).size()[dia.groupby(dia["patient_nbr"]).size()>=4])/len(dia.groupby(dia["patient_nbr"]).size())*100  # percentage patients with at least four visits
# Grouped the data by patient_nbr and used the size function to get how many hospital visits per each patient. I then
# further subset this to get all patients who had at least 4 visits, and took the length of this to get how many patients
# fit this condition. I divided by the length of the first series of unique patient numbers (total number of patients)
# to get a ratio, then multiplied by 100 to get a percentage.

# # 5.  List the top-10 most common diagnoses, based on the codes listed 
# #     collectively in the columns 'diag_1', 'diag_2', and 'diag_3'.
# #     Give your response as a Series with the diagnosis code as the 
# #     index and the number of occurances as the values, sorted by
# #     values from largest to smallest.  If more than one value could
# #     go in the 10th position, include all that could go in that 
# #     position.  (This is the usual "include ties" policy.)

q5 = pd.concat([dia['diag_1'], dia['diag_2'], dia['diag_3']], ignore_index=True)[
    pd.concat([dia['diag_1'], dia['diag_2'], dia['diag_3']],
              ignore_index=True) != "?"].value_counts()[:10]  # top-10 diagnoses plus any ties
# Concatenated the diagonals into one series and then removed the empty data by subsetting using a logical vector that
# was true when there was entered data. Then, I took the counts of each possible diagnosis and subset this list of counts
# to include only the 10 highest.

# # 6.  The 'age' in each record is given as a 10-year range of ages.  Assume
# #     that the age for a person is the middle of the range.  (For instance,
# #     those with 'age' [40,50) are assumed to be 45.)  Determine the average
# #     age for each classification in the column 'acarbose'.  Give your
# #     answer as a Series with the classification as index and averages as
# #     values, sorted from largest to smallest average.

q6 = dia["age"].map({
    '[0-10)'  : 5,
    '[10-20)' : 15,
    '[20-30)' : 25,
    '[30-40)' : 35,
    '[40-50)' : 45,
    '[50-60)' : 55,
    '[60-70)' : 65,
    '[70-80)' : 75,
    '[80-90)' : 85,
    '[90-100)': 95
}).groupby(dia["acarbose"]).mean()# Series of classifications and averages
# I used the map function to transform all the age ranges into the midpoint using a dictionary, then grouped
# the column of ages by acarbose and took the mean for each group.

# # 7.  Determine all medical specialties that have an average hospital stay
# #     (based on time_in_hospital) of at least 7 days.  Give a Series with
# #     specialty as index and average hospital stay as values, sorted from
# #     largest to smallest average stay.

q7 = dia["time_in_hospital"].groupby(dia["medical_specialty"]).mean()[
                 dia["time_in_hospital"].groupby(
                     dia["medical_specialty"]).mean() >= 7].sort_values(ascending=False)# Series of specialities and average stays
# Subsets the data, showing only the time in hospital column. Then, it groups by medical specialty, takes the average of the
# time for each group, subsets to include only those at least 7, and sorts in descending order.

# #  8. Three medications for type 2 diabetes are 'glipizide', 'glimepiride',
# #     and 'glyburide'.  There are columns in the data for each of these.
# #     Determine the number of records for which at least two of these
# #     are listed as 'Steady'.

q8 = len(dia.loc[(dia["glyburide"]=="Steady").astype(int)+
                  (dia["glipizide"]=="Steady").astype(int)+
                  (dia["glimepiride"]=="Steady").astype(int) > 1])  # number of records with at least two 'Steady'
# Subsets the data by getting logical values for whether each medicine is given steadily, then casting these values
# to integers (True=1, False=0) and adding them together. If this total is more than 1 (at least 2), then it returns
# true and includes this row in the subset. Then, it counts the length of the subset to get how many records fit this
# condition.

# #  9. Find the percentage of "time_in_hospital" accounted for by the top-75 
# #     patients in terms of number of times in file.  (Include all patients 
# #     that tie the 75th patient.)

q9 = np.sum(dia["time_in_hospital"].groupby(dia["patient_nbr"]).sum().sort_values(ascending=False)[:75])/np.sum(
    dia["time_in_hospital"])*100  # Percentage of time from top-75 patients
# Subsets the dataframe to show only the time and sorts by patient number, totaling the time for each patient. Then,
# it sorts this series in descending order and subsets it to only include the top 75 patients in terms of time, and sums
# these times together. Then, it is divided by the total amount of time in the dataframe and multiplied by 100 to be a
# percentage.

# # 10. What percentage records have reasons for admission ('admission_source_id') that correspond to some form of transfer from another care source?

q10 = None  # Percentage of admission by transfer


# # 11. The column 'discharge_disposition_id' gives codes for discharges.
# #     Determine the 7 codes that resulted in the greatest percentage of
# #     readmissions.  Give your answer as a Series with discharge code
# #     as index and readmission percentage as value, sorted by percentage
# #     from largest to smallest. The codes '<30' and '>30' in the 'readmitted' column indicate a readmission.

q11 = None  # Series of discharge codes and readmission percentages


# # 12. The columns from 'metformin' to 'citoglipton' are all medications, 
# #     with "Up", "Down", and "Steady" indicating the patient is taking that 
# #     medication.  For each of these medications, determine the average
# #     number of medications from this group that patients are taking (or have taken during any prior visit to the hospital).
# #     Give a Series of all medications with an average of at least 1.5,
# #     with the medications as index and averages as values, sorted 
# #     largest to smallest average.
# #     (Hint: df.columns gives the column names of the data frame df.)

q12 = None  # Series of medications and averages


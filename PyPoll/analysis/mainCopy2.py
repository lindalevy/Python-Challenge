# import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# columns in datasheet
# VoterID[0]	County[1]   Candidate[2]

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# create lists to use in manipulation to produce outputs
listvotes = list()  #list of all votes individually
unique_list=list()  # list of unique candidates, used to build outputdir and to print


with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row 
    next(csvreader, None)  # skip 


#initial fields and set starting value before commencing reading the rows
    countvotes = 0
    vpercent = 0

    # Loop through all rows
    for row in csvreader:
        # check if exists in unique_list or not 
        if row[2] not in unique_list: 
            unique_list.append(row[2])
    
        listvotes.append(row[2])  
        totalvotes = len(listvotes)  #total count of votes only
        results = {}  #build a file to hold candidate and # votes
    for i in unique_list:
        countvotes = listvotes.count(i) 
        vpercent = countvotes/totalvotes*100
        results[i] = vpercent

    print("Election Results")
    print("----------------")

    print(f"Total Votes: {totalvotes}")
    print("--------------------------")
    for candidate in (results):
        print({candidate}, ":")
    print(results)
# import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# columns in datasheet
# Date[0]	Profit/Losses[1]

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# create lists to use in manipulation to produce outputs
listvotes = list()
outputdir = {}
unique_list=list()

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row 
    next(csvreader, None)  # skip 


#initial fields and set starting value before commencing reading the rows

    # Loop through
    for row in csvreader:
        # check if exists in unique_list or not 
        if row[2] not in unique_list: 
            unique_list.append(row[2]) 

        listvotes.append(row[0])
        totalvotes = len(listvotes)

        
    print(unique_list)
    print("Election Results")
    print("----------------")
    print(f"Total Votes: {totalvotes}")
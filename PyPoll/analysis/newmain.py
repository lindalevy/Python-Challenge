# import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# columns in datasheet
# VoterID[0]	County[1]   Candidate[2]

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# create lists to use in manipulation to produce outputs
unique_candidate = {"candidiate": []}  # list of unique candidates, used to build outputdir and to print
outputdir= {"candidate":[], "percent":[0], "votes":[0]}

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row 
    next(csvreader, None)  # skip 

#initial fields and set starting value before commencing reading the rows
    countvotes = 0
    vpercent = 0

    # Loop through all rows
    for row in csvreader:
        voterid, county, candidate = row
        
        # check if exists in unique_list or not 
        if row[2] not in unique_candidate
            outputdir = {candidate}


current = len(outputdir)
print(curent)

    # find winner - this looked simple but this is having an issue with integers and strs. 
    # I have ignored this as this is not as important as getting the directory updated correctly
#    winner = max(outputdir, key=outputdir.get) 

    #time to create a file and all outcomes to the text file
    newfile= open("myPYPollResults.txt", "w")
    newfile.write("Election Results\n" + "--------------------\n")
    newfile.write("Total Votes: \n")
    newfile.write("--------------------\n")

    newfile.close()
 
    #start printing, and put spacing between to make it more readable
    # use this in the print function
    #        vpercent = "{:.3%}".format(vpercent)

    print ("    ")
    print("Election Results")
    print("----------------")
    print("    ")
    print(f"Total Votes: ")
    print("--------------------------")
    print( "   ")

    print("--------------------------")
    print( "   ")
#    print(f"Winner: {winner} ")


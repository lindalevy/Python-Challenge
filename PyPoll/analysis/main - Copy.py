
   # import the os module
# This will allow us to create file paths across operating systems
import os

#this might allow me to count the occurences for each element
from collections import Counter

# Module for reading CSV files
import csv
# columns in datasheet
# Date[0]	Profit/Losses[1]

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# create lists to use in manipulation to produce outputs
listvotes = list()
outputdir = {"candidate":[], "countedvotes": []}
unique_list= {"ucandidate":[]}

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row 
    next(csvreader, None)  # skip 


#initial fields and set starting value before commencing reading the rows

    # Loop through
    for row in csvreader:
        # check if exists in unique_list or not 
        voterid, county,rowcandidate = row
        if rowcandidate not in unique_list: 
            unique_list = {rowcandidate} 
    listvotes.append(rowcandidate)
  
    totalvotes = len(listvotes)  #total count of votes only
    
    d = Counter(listvotes)
        
    print ('{} has {} times'.format(rowcandidate, d[rowcandidate]))

    print(unique_list)
    print("Election Results")
    print("----------------")
    print(f"Total Votes: {totalvotes}")

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
    print(f"Total Votes: {totalvotes}")
    print("--------------------------")
    print( "   ")

    print("--------------------------")
    print( "   ")
#    print(f"Winner: {winner} ")

    print(outputdir)
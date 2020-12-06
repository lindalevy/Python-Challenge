# import the os module
# This will allow us to create file paths across operating systems
import os

import operator

# Module for reading CSV files
import csv
# columns in datasheet
# Voter ID	County	Candidate
#    0         1        2

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# create lists to use in manipulation to produce outputs
listvotes = list()   
unique_list = list()
outputdir = {"ocandidate":[], "ovotecounter":[], "opercent":[]}
outputdir2 = {}

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row 
    next(csvreader, None)  # skip 

    #initial fields and set starting value before commencing reading the rows

   
    # Loop through
    for row in csvreader:

        voterid, county,rowcandidate = row

        # check if exists in unique_list or not 
        if rowcandidate not in unique_list: 
            unique_list.append(rowcandidate)
   
        
    #create working fields for printing
        listvotes.append(rowcandidate)
    totalvotes = len(listvotes)
    #can we update outputdir
    for i in unique_list:
        x = listvotes.count(i)
        y = x/totalvotes*100
        outputdir[i] =listvotes.count(i), y
        outputdir2.update({i: y})
        
    # reading the directory to return the required information 
    #Gdate = max(outputdir, key= outputdir.get)
    #Sdate = min(outputdir, key= outputdir.get)
    #greatestprofit = max(outputdir.values())
    #avechange = round((listvotes/Amonths),2)

    # find winner 
   # winner = max(outputdir.items(), key=operator.itemgetter(1))[0]


    #time to create a file and all outcomes to the text file
    newfile= open("myPYPollResults.txt", "w")
    newfile.write("Election Results\n" + "--------------------\n")
    newfile.write(f"Total Votes: {totalvotes}\n")
    newfile.write("--------------------\n")

    newfile.write("--------------------------")
    newfile.write( "   ")
#    newfile.write(f"{winner}")
    newfile.close()
 
    #start printing, and put spacing between to make it more readable
    # use this in the print function
    #        vpercent = "{:.3%}".format(vpercent)
    print(outputdir2)
    print ("    ")
    print("Election Results")
    print("----------------")
    print("    ")
    print(f"Total Votes: {totalvotes}")
    print("--------------------------")
    print( "   ")
    for key, value in outputdir.items():
        print(key, ' : ', value)
    print("--------------------------")
    print( "   ")
#    print(f"Winner: {winner} ")

    print(outputdir)


# import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# columns in datasheet
# Voter ID	County	Candidate
#    0         1        2

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# create lists to use in manipulation to produce outputs
listvotes = list()  # a full list of each vote, storing just the candidate name  
candidate_options = list() #list of unique candidates

outputdir = {}  #unique candidates with their sum of votes
candidatepercentlist = list() #list of the percentage of votes per unique candidate

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row 
    next(csvreader, None)  # skip 

    #initial fields and set starting value before commencing reading the rows
   
    # Loop through
    for row in csvreader:

        # name the elemnts in the row
        voterid, county,rowcandidate = row

        #create list of candidates
        listvotes.append(rowcandidate)
        totalvotes = len(listvotes)
        
        # (our loop is "discovering" candidates as it goes)
        if rowcandidate not in candidate_options:
            # Add it to the list of candidates in the running
            candidate_options.append(rowcandidate)
            # And begin tracking that candidate's voter count
            outputdir[rowcandidate] = 0
            localcount =+ 1

        # Then add a vote to that candidate's count
        outputdir[rowcandidate] = outputdir[rowcandidate] + 1
        
    # find winner 
    winner = max(outputdir, key= outputdir.get)

    #what is the number of unique candidates
    unique = len(outputdir)
    unique = int(unique)

    #can we get lists, to calculate the percentage
    # first create 2 lists from the directory
    outputvalueslist = list(outputdir.values())
    outputdirkeylist = list(outputdir.keys())

    # calculate percentages, creating another list (candidate percentlist)
    for i in range(0, unique):
        percent = '{:.2%}'.format((outputvalueslist[i] / totalvotes))
        candidatepercentlist.append(percent)
    
    #time to create a file and write all outcomes to the text file
    newfile= open("myPYPollResults.txt", "w")
    newfile.write("Election Results\n" + "--------------------\n")
    newfile.write(f"Total Votes: {totalvotes}\n")
    newfile.write("--------------------\n")
    newfile.write("   ")
    newfile.write(f"Winner: {winner}\n")
    newfile.write( "   ")
    newfile.write("--------------------\n")
    for i in range(0, unique):
       newfile. write(f"    {outputdirkeylist[i]}    {candidatepercentlist[i]}   ({outputvalueslist[i]})\n")
    newfile.write("--------------------------")
    newfile.close()
 
    # print it out and go Home!
    print ("    ")
    print("Election Results")
    print("----------------")
    print("    ")
    print(f"Total Votes: {totalvotes}")
    print("--------------------------")
    print( "   ")
#   print winner
    print(f"Winner: {winner}")
    print( "   ")
    print("--------------------------")
    #print individual candiates results
    for i in range(0, unique):
        print(f"    {outputdirkeylist[i]}   {candidatepercentlist[i]}   ({outputvalueslist[i]}) ")
    print( "   ")
    print("--------------------------")

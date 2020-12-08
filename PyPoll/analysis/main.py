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
listvotes = list()   
candidate_options = list()
outputdir = {}

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
        
          # (In a way, our loop is "discovering" candidates as it goes)
        if rowcandidate not in candidate_options:
            # Add it to the list of candidates in the running
            candidate_options.append(rowcandidate)
            # And begin tracking that candidate's voter count
            outputdir[rowcandidate] = 0

        # Then add a vote to that candidate's count
        outputdir[rowcandidate] = outputdir[rowcandidate] + 1
        
    # find winner 
    winner = max(outputdir, key= outputdir.get)

    #time to create a file and all outcomes to the text file
    newfile= open("myPYPollResults.txt", "w")
    newfile.write("Election Results\n" + "--------------------\n")
    newfile.write(f"Total Votes: {totalvotes}\n")
    newfile.write("--------------------\n")
    newfile.write( "   ")
    newfile.write(f"Winner: {winner}\n")
    
    newfile.write( "   ")
    newfile.write("--------------------\n")
    newfile.writelines('{}:{}\n'.format(k,v) for k, v in outputdir.items()) 
    newfile.write("--------------------------")

    newfile.close()
 
    #start printing, and put spacing between to make it more readable
    # use this in the print function
    #        vpercent = "{:.3%}".format(vpercent)

    ## I have been unable to figure out in the time how to manage the percentages so this is not included

    print ("    ")
    print("Election Results")
    print("----------------")
    print("    ")
    print(f"Total Votes: {totalvotes}")
    print("--------------------------")
    print( "   ")
#   print winner
    print(f"Winner: {winner}")
    print("--------------------------")
    for key, value in outputdir.items():
        print(key, ' : ', value)

    print( "   ")
    print("--------------------------")

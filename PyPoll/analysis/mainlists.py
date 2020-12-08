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
candidate_votes = {}


with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row 
    next(csvreader, None)  # skip 

    #initial fields and set starting value before commencing reading the rows

   
    # Loop through
    for row in csvreader:
        #create working file all all votes
        candidate_name = row[2]
        listvotes.append(row[2])

        # check if exists in unique_list or not 
        #If the candidate does not match any existing candidate...
        # (In a way, our loop is "discovering" candidates as it goes)
        if candidate_name not in candidate_options: # Add it to the list of candidates in the running
            candidate_options.append(candidate_name) # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0 # Then add a vote to that candidate's count
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    totalvotes = len(listvotes)
    print("print total votes & unique list")
    print(totalvotes)

    print ("    ")
    print("Election Results")
    print("----------------")
    print("    ")
    print(f"Total Votes: {totalvotes}")
    
    # find winner 



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


 #   print(f"Winner: {winner} ")


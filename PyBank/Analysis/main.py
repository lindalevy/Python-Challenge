# import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# columns in datasheet
# Date[0]	Profit/Losses[1]

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# create lists to use in manipulation to produce outputs
listdate = list()   
listprofit = list()
outputdir = {}

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row 
    next(csvreader, None)  # skip 

    #initial fields and set starting value before commencing reading the rows
    totalprofit = 0
    index = 0
    lastprofit = 0
    totalchange = 0
    avechange = 0
    Amonths = 0
   
    # Loop through
    for row in csvreader:
       ## increment the index by 1
        index += 1
        
    #create working fields for printing
        profit = int(row[1])
        listdate.append(row[0])

        # calculate outcomes
        totalprofit += profit   
        totalmonths = len(listdate)

        # reduce month count by 1 as there is no change value for the first entry
        Amonths = totalmonths - 1

        if index > 1:
            profitchange = profit - lastprofit
            listprofit.append(profitchange)
            outputdir.update({row[0]: profitchange})
        lastprofit = profit

    # reading the directory to return the required information 
    Gdate = max(outputdir, key= outputdir.get)
    Sdate = min(outputdir, key= outputdir.get)
    greatestprofit = max(outputdir.values())
    smallestprofit = min(outputdir.values())
    totalchange = sum(listprofit) 
    avechange = round((totalchange/Amonths),2)
    
     #time to create a file and all outcomes to the text file
    newfile= open("myPYBankResults.txt", "w")
    newfile.write("Financial Analysis\n" + "--------------------\n")
    newfile.write(f"Total Months: {totalmonths}\n")
    newfile.write(f"For the entire period of {totalmonths} months:\n")
    newfile.write(f"The total profit: {totalprofit}\n")
    newfile.write(f"Average change of Profit/Losses: ${avechange}\n")
    newfile.write(f"Greatest Increase in Profits: {Gdate} - ${greatestprofit}\n")
    newfile.write(f"Greatest Decrease in Profits: {Sdate} - ${smallestprofit}\n")
    newfile.close()


    # printout findings
    print("Financial Analysis")  
    print("--------------------")       
    print (f"Total Months: {totalmonths}")
    print(f" for the entire period of {totalmonths} months: ")
    print(f"The total profit: ${totalprofit}")
    print(f"Average change of Profit/Losses: ${avechange}")
    print(f"Greatest Increase in Profits: {Gdate} - ${greatestprofit}")
    print(f"Greatest Decrease in Profits: {Sdate} - ${smallestprofit}")
   
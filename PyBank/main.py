# Importing dependencies, operating system (os) and comma separated variables (csv)
import os
import csv

# Routing to the source file for the elections database
csvfileroute = "budget_data.csv"

# File to output the results of the elections analysis to
outfile = "Analysis\My_Output.txt"

# Setting up a reader of the data file as a csv file
with open(csvfileroute, 'r') as csvfile:
    # Assigning read csv file to a variable - csv_reader
    csv_reader = csv.reader(csvfile, delimiter=",")
     
    # Isolating the header row to get to the data
    header = next(csv_reader)
    
    # Defining total number of months as an integer
    MntCnt = 0
    
    # Defining Profit/Losses variable as a list
    PL_rows = []

    # Initializing total amount of Profit/Losses variable as an integer
    total = 0
    # Setting up a for loop to compute Profit/Losses changes over period
    for row in csv_reader:
        MntCnt += 1                                # Total number of months
        total += int(row[1])                       # Total amount of Profit/Losses over period
        PL_rows.append([row[0], float(row[1])])    # Retrieving Profit/Losses data into a list
    # Defining amount change variable as a list
    Amt_chg = []
    
    # Defining date indexed to Profit/Losses changes variable as a list
    Date_chg = []
    
    # Defining average Profit/Losses changes variable as a list
    Avg_chg = 0#[]
    
    # Appending dates to a file called date change indexed to each Profit/Losses amount
    Date_chg.append(row[0])

    # Setting up a for loop for determining each Profit/Losses change
    for i in range(len(PL_rows)):
        # Using if statement to begin Profit/Losses change from row 2 after header row
        if i > 0:
            # Appending each row of Profit/Losses changes to a list
            Amt_chg.append(PL_rows[i][1] - PL_rows[i - 1][1])
    
    # Outputing average Profit/Losses changes over entire period
    Avg_chg = sum(Amt_chg)/len(Amt_chg)
    
    # Computing the maximum change indexed for associated date
    Max_chg_index = Amt_chg.index(max(Amt_chg)) + 1

    # Calculating maximum change date index list for each change
    Max_chg_date = PL_rows[Max_chg_index][0]
    
    # Computing the minimum change indexed for associated date
    Min_chg_index = Amt_chg.index(min(Amt_chg)) + 1

    # Calculating minimum change date index list for each change
    Min_chg_date = PL_rows[Min_chg_index][0]
    
    # Prepping variables for output of results to print file
    L1 = "Financial Analysis"
    L2 = "-" * 30
    L3 = "Total Months: {}".format(int(MntCnt))
    L4 = "Total: ${}".format(int(total))
    L5 = "Average Change: ${}".format(round(Avg_chg, 2))
    L6 = "Greatest Increase in Profits: {} (${})".format(Max_chg_date, max(Amt_chg))
    L7 = "Greatest Decrease in Profits: {} (${})".format(Min_chg_date, min(Amt_chg))
    LS = "\n"
    L_All = "{}{}{}{}{}{}{}{}{}{}{}{}{}".format(L1, LS, L2, LS, L3,LS,L4,LS,L5,LS,L6,LS,L7)
    print(L_All)

# Creating output file for Financial Analysis i.e. output file (outfile)
with open(outfile, 'w') as csvfile:
    csvfile.write(L_All)

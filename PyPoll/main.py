# Importing dependencies, operating system (os) and comma separated variables (csv)
import os
import csv

# Routing to the source file for the elections database
csvfile = "election_data.csv"

# File to output the results of the elections analysis to
outputfile = "Analysis\Election_Analysis.txt"

# Total votes variable as an integer
tot_votes = 0

# Candidate list variable as a list
cand_list = []

# Candidates votes variable as a dictionary key
cand_votes = {}

# Winning candidate variable as a string
win_cand = ""

# Winning candidate vote count as an integer
win_count = 0

# Setting up a reader of the data file as a csv file
with open(csvfile, 'r') as csv_file:
    # Assigning read csv file to a variable - csv_reader
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Isolating the header row to get to the data
    header = next(csv_reader)
    # Setting up a for loop to compute total vote count for each candidate
    for row in csv_reader:
        tot_votes += 1          # Total vote count for all candidates
        candidate = row[2]      # Selecting the 3rd column with candidates
        # Setting up if statement to populate candidates list
        if candidate not in cand_list:
            cand_list.append(candidate)
            cand_votes[candidate] = 0       # Candidates' vote count
        # Populating list with each candidate's total votes
        cand_votes[candidate] = cand_votes[candidate] + 1
# Setting up print output file for computation results
with open(outputfile, 'w')  as txtfile:
    elec_rslts = (
        f'\nElection Results\n'
        f'------------------------------\n'
        f'Total Votes: {tot_votes}\n'
        f'------------------------------\n')
    txtfile.write(elec_rslts)
    
    # Generating output file for printing to terminal
    Fin_Output = []

    # Setting up a for loop for determining each candidate's total vote
    for candidate in cand_votes:
        votes = cand_votes.get(candidate)                   # Retrieving each candidates total votes
        votes_pcntg = float(votes)/float(tot_votes)*100     # Computing each candidate's vote percentage
        # Using if statement to determine the winning candidate by maximum votes
        if (votes > win_count):
            win_count = votes
            win_cand = candidate
        voter_output = f'{candidate}: {votes_pcntg:.3f}% ({votes})\n'
        voter_output_term = f'{candidate}: {votes_pcntg:.3f}% ({votes})'
        
        # Outputing results file for print to terminal
        Fin_Output.append(voter_output_term)
        
        # Text output file
        txtfile.write(voter_output)
    # Setting up print output of winning candidate results to output file
    win_summ = (
        f"------------------------------\n"
        f'Winner: {win_cand}\n'
        f'------------------------------\n'
    )
    txtfile.write(win_summ)         # Output to print text file

    # Printing results to terminal
    elec_rslts = elec_rslts.rstrip()
    print(elec_rslts)
    for x in Fin_Output:
        print(x)
    print(win_summ)
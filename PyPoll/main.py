import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

# Lists to store data
all_votes = []
charles_votes = []
diana_votes = []
raymon_votes = []

with open(election_csv) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Reading in the header row
    csv_header = next(csvreader)
    
    # Append all the votes to a new list
    for row in csvreader:
        all_votes.append(row[2])
    
    # Append Charle's votes to a new list
    for value in all_votes:
        if value == "Charles Casper Stockham":
            charles_votes.append(value)
    
    # Append Diana's votes to a new list
    for value in all_votes:
        if value == "Diana DeGette":
            diana_votes.append(value)
    
    # Append Raymon's votes to a new list
    for value in all_votes:
        if value == "Raymon Anthony Doane":
            raymon_votes.append(value)
    
    # Calculate the percentage of total votes that Charles, Diana, and Raymon received
    charles_percent = round((len(charles_votes)/len(all_votes))*100 ,3)
    diana_percent = round((len(diana_votes)/len(all_votes))*100 ,3)
    raymon_percent = round((len(raymon_votes)/len(all_votes))*100 ,3)
    
    # If Diana received the most votes, declare her the winner
    if len(diana_votes) > len(charles_votes) and len(diana_votes) > len(raymon_votes):
        winner = "Diana DeGette"
    
    # If Charles received the most votes, declare him the winner
    if len(charles_votes) > len(diana_votes) and len(charles_votes) > len(raymon_votes):
        winner = "Charles Casper Stockham"
    
    # If Raymon received the most votes, declare him the winner
    if len(raymon_votes) > len(diana_votes) and len(raymon_votes) > len(charles_votes):
        winner = "Raymon Anthony Doane"
    
    # Print the election results
    print("Election Results")
    print("-----------------------")
    print(f'Total Votes: {len(all_votes)}')
    print("-----------------------")
    print(f'Charles Casper Stockham: {charles_percent}% ({len(charles_votes)})')
    print(f'Diana DeGette: {diana_percent}% ({len(diana_votes)})')
    print(f'Raymon Anthony Doane: {raymon_percent}% ({len(raymon_votes)})')
    print("-----------------------")
    print(f'Winner: {winner}')
    
output_file = os.path.join("Analysis", "results.txt")

# Write the election results to a new text file
with open(output_file, "w") as datafile:
    
    datafile.write("Election Results\n")
    datafile.write("-----------------------")
    datafile.write(f'Total Votes: {len(all_votes)}\n')
    datafile.write("-----------------------\n")
    datafile.write(f'Charles Casper Stockham: {charles_percent}% ({len(charles_votes)})\n')
    datafile.write(f'Diana DeGette: {diana_percent}% ({len(diana_votes)})\n')
    datafile.write(f'Raymon Anthony Doane: {raymon_percent}% ({len(raymon_votes)})\n')
    datafile.write("-----------------------\n")
    datafile.write(f'Winner: {winner}\n')
        
    
        
    

    
    
    

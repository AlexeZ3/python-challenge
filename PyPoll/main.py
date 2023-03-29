import os

# Module for reading CSV files
import csv


election_data_csv = os.path.join('resources', 'election_data.csv')
file_to_output = os.path.join('analysis', 'election_data.txt')

totalVotes = 0 
votesPerCandidate = {}

# open up election_data
with open(election_data_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        totalVotes += 1
        if row[2] not in votesPerCandidate:
            votesPerCandidate[row[2]] = 1
        else:
            votesPerCandidate[row[2]] += 1   
        
        


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalVotes))
print("-------------------------")

for candidate, votes in votesPerCandidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    
print("-------------------------") 

winner = max(votesPerCandidate, key=votesPerCandidate.get)

print(f"Winner: {winner}")

# now write this to an output file

output = f'''Election Results \n
------------------------- \n
Total Votes: {str(totalVotes)} \n
------------------------- \n
------------------------- \n 
"Winner: {winner} \n
-------------------------'''

with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("---------------------------------------\n")
    txt_file.write("Total Vote: " + str(totalVotes) + "\n")
    txt_file.write("---------------------------------------\n")
    for candidate, votes in votesPerCandidate.items():
        txt_file.write(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")" "\n")
    txt_file.write("---------------------------------------\n")
    txt_file.write("The winner is: " + winner + "\n")
    txt_file.write("---------------------------------------\n")


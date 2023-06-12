import os
import csv

#LOCATES CSV FILE TO READ
csv_path = os.path.join("Resources", "election_data.csv")

#CREATES LISTS OF BLANK DATA
ballot_id = []
county = []
candidate = []
winner = []

#READS CSV FILE - CLASS DEMONSTRATION
with open(csv_path, encoding='UTF-8') as csvfile:
    csv_read = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_read)

    #CREATES LISTS
    for row in csv_read:
        ballot_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])


#TOTAL NUMBER OF VOTES
vote_count = len(ballot_id)

#ELIMINATES DUPLICATES
#REFERENCED STACKOVERFLOW 7961363
candidate_names = sorted(list(set(candidate)))
    
print("Election Results")
print("--------------------------")
print(f"Total Votes: {vote_count}")
print("--------------------------")

#PRINT CANDIDATES WITH VOTE COUNT AND PERCENT - FLUID
count = 0
for person in candidate_names:
    vote_num = candidate.count(candidate_names[count])
    vote_percent = round((vote_num/vote_count)*100, 3)
    winner.append(vote_num)
    print(f"{candidate_names[count]}: {vote_percent}% ({vote_num})")
    count = count + 1

print("--------------------------")
#print winner with most votes
lead_candidate = max(winner)
win_count = (winner.index(lead_candidate))
print(f"Winner: {candidate_names[win_count]}")
print("--------------------------")

#SAVE FOR LATER WHEN FORMULAS ALL WORKING
#output_path = os.path.join("analysis", "election_results.csv")

#with open(output_path, "w", newline='') as csvfile:
    #csv_write = csv.writer(csvfile, delimiter=',')
    #csv_write.writerow("Election Results")
    #csv_write.writerow("----------------------------")
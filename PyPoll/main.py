import os
import csv

csv_path = os.path.join("Resources", "election_data.csv")

#CREATES LISTS OF BLANK DATA
ballot_id = []
county = []
candidate = []

with open(csv_path, encoding='UTF-8') as csvfile:
    csv_read = csv.reader(csvfile, delimiter=',')

    for row in csv_read:
        ballot_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#POP(0) TO REMOVE TITLES FROM LISTS
ballot_id.pop(0)
county.pop(0)
candidate.pop(0)

#TOTAL NUMBER OF VOTES
vote_count = len(ballot_id)

#ELIMINATES DUPLICATES
#REFERENCED STACKOVERFLOW 7961363
candidate_names = sorted(list(set(candidate)))


print("Election Results")
print("--------------------------")
print(f"Total Votes: {vote_count}")
print("--------------------------")
#print candidates c/ percent won and vote count
print(f"{candidate_names[0]}: ")
print(f"{candidate_names[1]}: ")
print(f"{candidate_names[2]}: ")
print("--------------------------")
#print winner with most votes
print(f"Winner: ")
print("--------------------------")
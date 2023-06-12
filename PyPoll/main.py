import os
import csv

#LOCATES CSV FILE TO READ
csv_path = os.path.join("Resources", "election_data.csv")

#CREATES LISTS OF BLANK DATA
ballot_id = []
county = []
candidate = []

#READS CSV FILE - CLASS DEMONSTRATION
with open(csv_path, encoding='UTF-8') as csvfile:
    csv_read = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_read)

    count = 0
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
#(len(candidate_names))
  
print("Election Results")
print("--------------------------")
print(f"Total Votes: {vote_count}")
print("--------------------------")
#print candidates c/ percent won and vote count
print(f"{candidate_names[0]}: ")  # <-- works for this assignment
print(f"{candidate_names[1]}: ")  #     but not very flexible for additional
print(f"{candidate_names[2]}: ")  #     candidates or csv files (loop?)
print("--------------------------")
#print winner with most votes
print(f"Winner: ")
print("--------------------------")

#SAVE FOR LATER WHEN FORMULAS ALL WORKING
#output_path = os.path.join("analysis", "election_results.csv")

#with open(output_path, "w", newline='') as csvfile:
    #csv_write = csv.writer(csvfile, delimiter=',')
    #csv_write.writerow("Election Results")
    #csv_write.writerow("----------------------------")
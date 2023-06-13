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
tot_votes = f"Total Votes: {vote_count}"

#ELIMINATES DUPLICATES
#REFERENCED STACKOVERFLOW 7961363
candidate_names = sorted(list(set(candidate)))

divider = "----------------------------"

def output(message):
    message("Election Results")
    message(divider)
    message(tot_votes)
    message(divider)
    #PRINT CANDIDATES WITH VOTE COUNT & PERCENT - FLUID
    count = 0
    for person in candidate_names:
        vote_num = candidate.count(candidate_names[count])
        vote_percent = round((vote_num/vote_count)*100, 3)
        winner.append(vote_num)
        message(f"{candidate_names[count]}: {vote_percent}% ({vote_num})")
        count = count + 1
    message(divider)
    #IDENTIFIES MAX VOTE COUNT
    lead_candidate = max(winner)
    #IDENTIFIES INDEX FOR MAX VOTE TO MATCH WITH CANDIDATE
    win_count = (winner.index(lead_candidate))
    leads = f"Winner: {candidate_names[win_count]}"
    message(leads)
    message(divider)

output(print)

#CSV PATH TO CREATE
output_path = os.path.join("analysis", "election_results.csv")

#REFERENCED STACKOVERFLOW 15129567 FOR [] 1 COLUMN
with open(output_path, "w", newline='') as csvfile:
    csv_write = csv.writer(csvfile, delimiter=',')
    w_csv = csv_write.writerow
    w_csv(["Election Results"])
    w_csv([divider])
    w_csv([tot_votes])
    w_csv([divider])
    count = 0
    for person in candidate_names:
        vote_num = candidate.count(candidate_names[count])
        vote_percent = round((vote_num/vote_count)*100, 3)
        winner.append(vote_num)
        w_csv([f"{candidate_names[count]}: {vote_percent}% ({vote_num})"])
        count = count + 1
    w_csv([divider])
    #print winner with most votes
    lead_candidate = max(winner)
    win_count = (winner.index(lead_candidate))
    leads = f"Winner: {candidate_names[win_count]}"
    w_csv([leads])
    w_csv([divider])
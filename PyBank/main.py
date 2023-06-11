import os
import csv

csv_path = os.path.join("..", "Resources", "budget_data.csv")

#creates blank lists for data
bank_date = []
win_loss = []

with open(csv_path, encoding='UTF-8') as csvfile:
    csv_read = csv.reader(csvfile, delimiter=',')

    for row in csv_read:
        bank_date.append(row[0])
        win_loss.append(row[1])

    #pop[0] to remove title from lists
    bank_date.pop[0]
    win_loss.pop[0]
    
    #calculates number of rows
    total_mth = len(bank_date)
    total_money = len(win_loss)

    #calculates net amount profit/loss
    sum_money = sum(win_loss)
    
    #calculates average changes
    avg_money = sum_money/total_money
    
    #calculates greatest increase/decrese
    max_win = max(win_loss)
    max_loss = min(win_loss)

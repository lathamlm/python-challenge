import os
import csv

csv_path = os.path.join("Resources", "budget_data.csv")

#CREATES LISTS FOR BLANK DATA
bank_date = []
win_loss = []

with open(csv_path, encoding='UTF-8') as csvfile:
    csv_read = csv.reader(csvfile, delimiter=',')

    for row in csv_read:
        bank_date.append(row[0])
        win_loss.append(row[1])
        

    #POP(0) TO REMOVE TITLES FROM LISTS
    bank_date.pop(0)
    win_loss.pop(0)
    
    #CALCULATES NUMBER OF ROWS
    total_mth = len(bank_date)
    total_money = len(win_loss)

    #calculates net amount profit/loss - NEED TO MAKE INTEGER
    #sum_money = sum(win_loss)
    #print(sum_money)
    #calculates average changes
    #avg_money = sum_money/total_money
    
    #calculates greatest increase/decrese
    #max_win = max(win_loss1)
    #max_loss = min(win_loss1)

print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {total_mth}")
#print(sum_money)
print(f"Total: ")
#print(avg_money)
print(f"Average Change: ")
#print(max_win)
print(f"Greatest Increase in Profits: ")
#print(max_loss)
print(f"Greatest Decrease in Profits: ")

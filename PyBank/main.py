import os
import csv

#LOCATES CSV FILE TO READ
csv_path = os.path.join("Resources", "budget_data.csv")

#CREATES LISTS FOR BLANK DATA
bank_date = []
win_loss = []
win_loss_diff = []

#READS CSV FILE - CLASS DEMONSTRATION
with open(csv_path, encoding='UTF-8') as csvfile:
    csv_read = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_read)

    #CREATES LISTS
    for row in csv_read:
        bank_date.append(row[0])
        win_loss.append(row[1])
    
#CALCULATES NUMBER OF ROWS
total_mth = len(bank_date)
total_money = len(win_loss)

#CONVERTS STRING TO INTEGER
#REFERENCED STACKOVERFLOW 43769886
money_int = [int(x) for x in win_loss]

#CALCULATES NET PROFIT/LOSS
sum_money = sum(money_int)

#CREATES LIST FOR DAY TO DAY CHANGES - USED FOR FINDING AVG, MAX, AND MIN
#COUNT = 1 TO AVOID ERROR WHEN SUBTRACTING
count = 1
for value in money_int:
    #AVOIDS GOING OUT OF RANGE SINCE VALUE STARTS AT 1 INSTEAD OF 0
    if count == len(money_int):
        exit
    #SUBTRACTS CURRENT DAY FROM PRIOR TO CAPTURE PROFIT/LOSS AND STORES IN LIST
    else:
        diff = (money_int[count]) - (money_int[(count-1)])
        win_loss_diff.append(diff)
    count = count + 1

#CALCULATES AVERAGE PROFIT/LOSS CHANGES
avg_money = round((sum(win_loss_diff))/(len(win_loss_diff)),2)

#DETERMINES GREATEST INCREASE AND GREATEST DECREASE
max_win = max(win_loss_diff)
max_loss = min(win_loss_diff)

#IDENTIFIES INDEX OF GREATEST VALUES FOR DATE IDENTIFICATION
win_index = win_loss_diff.index(max_win)
loss_index = win_loss_diff.index(max_loss)

#TOTAL MONTHS
month_length = f"Total Months: {total_mth}"

#SUM MONEY
money_sum = f"Total: ${sum_money}"

#AVERAGE DAILY CHANGE
money_avg = f"Average Change: ${avg_money}"

#GREATEST INCREASE (ADD 1 TO INDEX TO COMPENSATE FOR COUNT STARTING AT 1 IN FOR LOOP)
great_up = f"Greatest Increase in Profits: {bank_date[win_index+1]} (${max_win})"

#GREATEST DECREASE (ADD 1 TO INDEX TO COMPENSATE FOR COUNT STARTING AT 1 IN FOR LOOP)
great_down = f"Greatest Decrease in Profits: {bank_date[loss_index+1]} (${max_loss})"

#PRINT TO TERMINAL
print("Financial Analysis")
print("------------------------------")
print(month_length)
print(money_sum)
print(money_avg)
print(great_up)
print(great_down)


#CSV PATH TO CREATE
output_path = os.path.join("analysis", "budget_results.csv")

#REFERENCED STACKOVERFLOW 15129567 FOR [] 1 COLUMN
with open(output_path, "w", newline ='') as csvfile:
    csv_write = csv.writer(csvfile, delimiter=',')
    csv_write.writerow(["Financial Analysis", ""])
    csv_write.writerow(["-------------------------------"])
    csv_write.writerow([month_length])
    csv_write.writerow([money_sum])
    csv_write.writerow([money_avg])
    csv_write.writerow([great_up])
    csv_write.writerow([great_down])
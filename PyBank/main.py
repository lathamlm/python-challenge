import os
import csv

#LOCATES CSV FILE TO READ
csv_path = os.path.join("Resources", "budget_data.csv")

#CREATES LISTS FOR BLANK DATA
bank_date = []
win_loss = []

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

    #calculates average changes - WRONG AVERAGE
    #avg_money = sum_money/int(total_money)
    #print(avg_money)
 

    #calculates greatest increase/decrease day over day (not total)
        

print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {total_mth}")
#print(sum_money)
print(f"Total: ${sum_money}")
#print(avg_money)
print(f"Average Change: ")
#print(max_win)
print(f"Greatest Increase in Profits: ")
#print(max_loss)
print(f"Greatest Decrease in Profits: ")

#CSV TO CREATE
#output_path = os.path.join("analysis", "budget_results.csv")

#with open(output_path, "w", newline ='') as csvfile:
    #csv_write = csv.writer(csvfile, delimiter=',')
    #csv_write.writerow("Financial Analysis")
    #csv_write.writerow("-------------------------------")

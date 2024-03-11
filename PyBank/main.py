import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")

#Lists to store data
dates = []
profit_loss = []
change = []

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Reading in the header row
    csv_header = next(csvreader)
    
    # Append dates to a list
    # Append profit/loss data to a list
    for row in csvreader:
        dates.append(row[0])
    
        profit_loss.append(int(row[1]))
        
    
    # Variable to hold the total number of months
    total_months = len(dates)
    
    # Variable to hold the net total of the profits/losses
    net_total = sum(profit_loss)
    
    # Calculate the changes in profit/loss and append to list
    for value in range(len(profit_loss) - 1):
        
        profit_loss_change = profit_loss[value + 1] - profit_loss[value]
        change.append(profit_loss_change)
        
    # Calculate the average of the changes
    avg_change = round(sum(change)/len(change), 2)
    
    # Find the greatest increase and decrease
    greatest_increase = max(change)
    greatest_decrease = min(change)
    
    # Find the month with greatest increase and decrease
    greatest_increase_month = dates[change.index(greatest_increase) + 1]
    greatest_decrease_month = dates[change.index(greatest_decrease) + 1]
    
    # Print results
    print("Financial Analysis /n")
    print("--------------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: ${net_total}')
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
    
output_file = os.path.join("Analysis", "results.txt")

with open(output_file, "w") as datafile:
    # Write the results to a new text file
    
    datafile.write("Financial Analysis\n")
    datafile.write("--------------------------------\n")
    datafile.write(f'Total Months: {total_months}\n')
    datafile.write(f'Total: ${net_total}\n')
    datafile.write(f'Average Change: ${avg_change}\n')
    datafile.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n')
    datafile.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n')
    

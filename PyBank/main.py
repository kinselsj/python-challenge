import os
import csv


# Path to collect data
budget_csv = os.path.join('budget_data.csv')



# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    months = []
    header = next(csvreader)
    
    net_pl = []
    change_pl = []
        # Loop through the data
    for row in csvreader:
      
#The total number of months included in the dataset
        
        months.append(row[0])

#The net total amount of "Profit/Losses" over the entire period
        net_pl.append(float(row[1]))

#The average of the changes in "Profit/Losses" over the entire period
    for i in range(1,len(net_pl)):
        change_pl.append(net_pl[i] - net_pl[i-1])
        average_pl = sum(change_pl) / len(change_pl)
#The greatest increase in profits (date and amount) over the entire period
high_profit = max(change_pl)
high_month = str(months[change_pl.index(max(change_pl))+1])
#The greatest decrease in losses (date and amount) over the entire period
low_proft = min(change_pl)
low_month = str(months[change_pl.index(min(change_pl))+1])

print ("Financial Analysis")
print ("-------------------------------")
print (f"Total Months: {len(months)}")
print (f"Total: ${round(sum(net_pl))}")
print (f"Average Change: ${round(average_pl,2)}")
print (f"Greatest Increase in Profits: {high_month}, (${round(high_profit)})")
print (f"Greatest Decrease in Profits: {low_month}, (${round(low_proft)})")

f= open("Financial Analysis", 'w')
f.write ("-------------------------------\n")
f.write (f"Total Months: {len(months)}\n")
f.write (f"Total: ${round(sum(net_pl))}\n")
f.write (f"Average Change: ${round(average_pl,2)}\n")
f.write (f"Greatest Increase in Profits: {high_month}, (${round(high_profit)})\n")
f.write (f"Greatest Decrease in Profits: {low_month}, (${round(low_proft)})\n")
f.close()
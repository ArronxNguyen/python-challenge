# Import module allowing the creation of dynamic path to external files
import os
# Import module to translate the object being opened by python
import csv

#Set the path containing CSV file c/Users/arron/Learnpython/python-challenge/PyBank
csvpath = os.path.join('Resources','PyBank_Resources_budget_data.csv')

# Set variables required for calculations
#total variables
total_months = 0
total_profit_loss = 0
#change variables
prev_profit_loss = 0
monthly_change = 0
total_month_change = 0
average_month_change = 0
#greatest variables values
greatest_increase = 0
greatest_decrease = 0
#greatest variables months
greatest_increase_month = ""


# Open the CSV, instruct Python that each ',' should be moved to an new collumn for a row
with open(csvpath, newline='')as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Instruct Python to read the header row first
    csv_header = next(csvreader)
        #print(csv_header) -tested 2 headers -
    
    # Read each row of data after the header as a row
    for row in csvreader:
        # count the total_months, 
        # by using += add 1 to total_months for every row found after reader  
        total_months += 1
        #print(total_months) -tested 86 rows found - 
        
        # Tally up the total net profit/loss, by using +=
        total_profit_loss += int(row[1])
        #print(total_profit_loss)- tested last row total = 38382578 -
        
        # calculate the change in profit/loss between months. 
        # If the total months is not the header than monthly_change is next row - prev_profit_loss
        if row[1] == 'Profit/Losses':
            pass
        else:
          monthly_change = int(row[1]) - prev_profit_loss
        
        # Sum up the total_month_change, suming the values for monthly_change
        total_month_change += monthly_change        
                
        # what was the profit/loss value for previous month? 
        #(row[1]or column 2), find to prev_profit_loss
        prev_profit_loss = int(row[1])
        #print(prev_profit_loss) -tested-
                      
        # Find the largest monthly_change
        # loop through array elements from second row
        # and compare every element with the current max, to find the greatest max
        if monthly_change > greatest_increase:
            greatest_increase = monthly_change
            #find the corrsponding date
            greatest_increase_month = row[0]
        
        # Find the smallest monthly_change, reverse of finding max
        if monthly_change < greatest_decrease:
            greatest_decrease = monthly_change
            #find the corrsponding date
            greatest_decrease_month = (row[0])

# calculate the average in monthly change. 
# -1 row as first month does not have a change value     
average_month_change = total_month_change / (total_months - 1)


# Print the analysis. 
# Use f-string to convert data into printed sequence without continuely difining change in data type
print("Financial Analysis")
print('---------------------------------------------------')
print (f"Total: {int(total_months)} months")
print (f"Total: ${int(total_profit_loss)}")
print ("Average Change: $" + "{:.2f}".format(average_month_change));
print (f"Greatest Increase in Profits: {str(greatest_increase_month)}  (${int(greatest_increase)})")
print (f"Greatest Decrease in Profits: {str(greatest_decrease_month)}  (${int(greatest_decrease)})")

with open ("PyBank_Analysis.txt","w") as PyBank_Analysis:
    print ("Financial Analysis\n", file=PyBank_Analysis)
    print ("---------------------------------------------------\n", file=PyBank_Analysis)
    print (f"Total: {int(total_months)} months\n", file=PyBank_Analysis)
    print (f"Total: ${int(total_profit_loss)}\n", file=PyBank_Analysis)
    print (("Average Change: $" + "{:.2f}".format(average_month_change))+"\n", file=PyBank_Analysis);
    print (f"Greatest Increase in Profits: {str(greatest_increase_month)} (${int(greatest_increase)})\n",file=PyBank_Analysis)
    print (f"Greatest Decrease in Profits: {str(greatest_decrease_month)} (${int(greatest_decrease)})\n",file=PyBank_Analysis)      
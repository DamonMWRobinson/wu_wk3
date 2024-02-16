# Set up dependencies
import os
import csv

# Read in CSV file
budget = os.path.join("Resources","budget_data.csv")
os.path.join("Resources","budget_data.csv")

# Sets up output file
output_file = os.path.join("Resources","budget_analysis.txt")

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Declares variables and reads in csv file
total_months = 0
monthly_changes=[]
net_changes_list =[]
greatest_inc = ["",0]
greatest_decr=["",9999999999]
net_total=0

with open(budget) as fin_data:
    reader = csv.reader(fin_data)
    header = next(reader)

    first_row = next(reader)
    total_months = total_months + 1
    net_total += int(first_row[1])
    prev_net = int(first_row[1])

    
    # Loops through rows in reader for vote count and candidate name

    for row in reader:

        total_months += 1
        net_total += int(row[1])

        # Track the net change

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_changes_list += [net_change]
        monthly_changes += [row[0]]

        # calculate the greatest increase
        if net_change > greatest_inc[1]:
            greatest_inc[0] = row[0]
            greatest_inc[1] = net_change


        if net_change < greatest_decr[1]:
            greatest_decr[0] = row[0]
            greatest_decr[1] = net_change


# Net monthly average calculation
net_monthly_avg = sum(net_changes_list)/len(net_changes_list)

# Text file output
output = (
    f"Financial Analysis\n" 
    f"--------------------------\n"
    f"Total Months: {total_months} months\n"
    f"Total: $  {net_total} \n"
    f"Average Change: $ {net_monthly_avg}  \n" 
    f"Greatest Increase in Profits: {greatest_inc[0]}  (${greatest_inc[1]}) \n"
    f"Greatest Decrease in Profits: {greatest_decr[0]} (${greatest_decr[1]}) \n" 
     )

# Terminal output          
print(output)

with open(output_file, "w") as txt_file:
    txt_file.write(output)
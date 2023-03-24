import os
import csv

file = os.path.join("Resources", "budget_data.csv")
file_output = os.path.join("analysis", "Return_budget.txt")
total_months = 0
month_change = []
change_list = []
increase = ["",0]
decrease = ["",99999999]
net_total = 0

with open(file) as finance:
    csvreader = csv.reader(finance, delimiter = ",")
    header = next(csvreader)
    total_months += 1
    first = next(csvreader)
    net_total += int(first[1])
    previous_net = int(first[1])

    for row in csvreader:
        total_months += 1
        net_total += int(first[1])
        previous_net = int(first[1])

        #track the net change

        net_change = int(row[1]) - previous_net
        change_list.append(net_change)
        month_change.append(row[0])

        #calculate the increase

        if (net_change > increase[1]):
            increase[0] = row[0]
            increase[1] = net_change

            #calculate the decrease

        if (net_change < decrease[1]):
            decrease[0] = row[0]
            decrease[1] = net_change

            #calculate the average

        average = round(int(net_change) / len(change_list), 2)

            #generate summary

        output = ( f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total Revenue: ${net_total}\n"
        f"Average Revenue Change: ${average}\n"
        f"Greatest Increase in Revenue: {increase[0]} (${increase[1]})\n"
        f"Greatest Decrease in Revenue: {decrease[0]} (${decrease[1]})\n")

        #print the output to the terminal

        print(output)

        # Export the results to text file
        
with open(file_output, "w") as txt_file:
    txt_file.write(output)
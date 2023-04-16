import csv, os
from datetime import datetime
from pprint import pprint

# Set path to the target csv file
dirname = os.path.dirname(__file__)
budget_csv = os.path.join(dirname, 'Resources\\budget_data.csv')

# cast csv data as appropriate type
# datetime source: https://stackabuse.com/how-to-format-dates-in-python/
def month_counter(budget_csv):
    #date = str(budget_csv[0])                   #datetime.strptime(budget_csv[0], '%b-%y')  # date formatting not used for getting the month count.


    # read through the full csv file
    with open(budget_csv, 'r') as csvfile:
        # Split on delimiter
        csvreader = csv.reader(csvfile, delimiter= ',')

        # skip the header for performing operations on row data
        header = next(csvreader)


        # create dictionary for storing unique month values
        months_dict = {}
        # loop through the data to get unique month-yr values
        # source code: https://stackoverflow.com/questions/53221498/python-count-unique-value-in-row-csv
        for row in csvreader:
            if row[0] not in months_dict:
                months_dict[row[0]] = 0
            months_dict[row[0]] = months_dict[row[0]] + 1

        #output the count of rows in the unique months_dict with assignment formatting:
        print("\nFinancial Analysis\n---------------------------- \n")
        print("Total Months: " + str(len(months_dict)))

def net_total(budget_csv):
    #date = str(budget_csv[0])                   #datetime.strptime(budget_csv[0], '%b-%y')  # date formatting not used for getting the month count.
    #profit_loss = budget_csv[1]
    #print(type(profit_loss))

 # read through the full csv file
    with open(budget_csv, 'r') as csvfile:
        # Split on delimiter
        csvreader = csv.reader(csvfile, delimiter= ',')
        profit_data = list(csvreader)
        csvfile.close


        #create list for storing the csv profit/loss int numbers
        prof_list = []
        #print(profit_data)
        for row in profit_data[1:]:
            #print(int(row[1]))
            prof_list.append(int(row[1]))
        
        print("\nTotal: $" + str(sum(prof_list)) + "\n")



def net_changes(budget_csv):
    #date = str(budget_csv[0])                   #datetime.strptime(budget_csv[0], '%b-%y')  # date formatting not used for getting the month count.
    #profit_loss = budget_csv[1]
    #print(type(profit_loss))

 # read through the full csv file
    with open(budget_csv, 'r') as csvfile:
        # Split on delimiter
        csvreader = csv.reader(csvfile, delimiter= ',')
        new_list = list(csvreader)
        
        prev_i = 0
        sum_change = 0
        max_change = 0
        max_row = ''
        min_change = 0
        min_row = ''
        for i in new_list:
            try:
                if prev_i == 0:
                    change = 0
                    i.append(change)
                    prev_i = int(i[1])
                    # print(prev_i)

                else:
                    change = int(i[1]) - int(prev_i)
                    # print(change)
                    i.append(change)
                    prev_i = int(i[1])
                    sum_change = sum_change + change
                    if change > max_change:
                        max_change = change
                        max_row = i[0]
                    else:
                        pass

                    if change < min_change:
                        min_change = change
                        min_row = i[0]
                    else:
                        pass

                    # print(prev_i)
            except:
                pass

        # pprint((new_list))
        print("Average Change: $" + str(round(sum_change/len(new_list[1:]), 2)) + "\n")

        print("Greatest Increase in Profits: " + str(max_row) + " ($" + str(round(max_change, 0)) + ")\n")
        print("Greatest Decrease in Profits: " + str(min_row) + " ($" + str(round(min_change, 0)) + ")\n")


# run first part of analysis output: count of unique month-yr values in the csv
month_counter(budget_csv)

# run second part of analysis output: net total amount of profit/losses over the entire period (dataset)
net_total(budget_csv)

# run third part of anaylsis output: average monthly change, greatest increase in profits, and greatest decrease in profits
net_changes(budget_csv)
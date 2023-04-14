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
   # profit_loss = int(budget_csv[1])

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
        # pprint(new_list)
        
        for i in new_list:
            try:
                # date = str(row[0])
                profit = int(i[1])
                # # monthly_change = profit - int(row[i-1])

                i.append(profit)
                # print(profit)
                # row.append(profit)
                
                # new_list.append(row)
            except:
                pass

        pprint(new_list)


        # profit_data = list(csvfile)
        # csvfile.close
        # print(profit_data)




        # for row in profit_data[1:]:
        #     profit_data[3] = 
        #     print(profit_data[1:])
        #     #profit_data[3] = 


        # #create dictionary for storing the csv data
        # #Source code: https://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file
        # with open(budget_csv, 'r') as csvfile:
        #     reader = csv.reader(csvfile)
        #     with open('budget_changes_csv', 'w') as newfile:
        #         writer = csv.writer(newfile)
        #         changes_list = [rows[0]:rows[1] for rows in reader]

        #         # add calculated column of difference between row and row -1
        #         # source: https://stackoverflow.com/questions/65958081/adding-a-new-column-to-and-existing-dictionary-in-python
        #         # for row in changes_dict:
        #         #     print(row)


        #         print(newfile)



        # _list = []
        # #print(profit_data)
        # for row in profit_data[:]:
        #     #print(int(row[1]))
        #     prof_list.append(int(row[1]))
        
        # print("Average Change: $")


# run first part of analysis output: count of unique month-yr values in the csv
month_counter(budget_csv)

# run second part of analysis output: net total amount of profit/losses over the entire period (dataset)
net_total(budget_csv)

# run third part of anaylsis output: average monthly change, greatest increase in profits, and greatest decrease in profits
net_changes(budget_csv)
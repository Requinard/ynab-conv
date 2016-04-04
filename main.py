import csv

"""
Example format: Date,Payee,Category,Memo,Outflow,Inflow
"""

output_file = []

with open("ing.csv", 'r') as csvfile:


        print(row)
        print(new_row)

with open("ynab.csv", "w") as csvfile:
    csvfile.write("Date,Payee,Category,Memo,Outflow,Inflow\r")
    for row in output_file:
        for item in row:
            csvfile.write("{0},".format(item))
        csvfile.write("\r")



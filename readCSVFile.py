import csv
with open("semester2.csv") as filecsv:
    readCSV = csv.reader(filecsv)
    for row in readCSV:
        print(row)
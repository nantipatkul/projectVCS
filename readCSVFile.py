import csv
with open("student.csv") as filecsv:
    readCSV = csv.reader(filecsv)
    for row in readCSV:
        print(row)
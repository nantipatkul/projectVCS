import csv

def showCode(codelist):
    for data in codelist:
        print(data)

datalist = []
with open("semester2.csv") as filecsv:
    readCSV = csv.reader(filecsv)
    for row in readCSV:
        datalist.append(row[0])

showCode(datalist)

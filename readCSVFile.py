import csv

def showSubjectCode(subjectCode):
    print(subjectCode)

with open("semester3.csv") as filecsv:
    readCSV = csv.reader(filecsv)
    for row in readCSV:
        showSubjectCode(row[0])

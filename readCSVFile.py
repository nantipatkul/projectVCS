import csv

def showSubjectCode(subjectCode):
    for code in subjectCode:
        print(code)


with open("semester3.csv") as filecsv:
    readCSV = csv.reader(filecsv)
    for row in readCSV:
        print(row)
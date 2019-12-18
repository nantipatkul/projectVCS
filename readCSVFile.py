import csv

def showSubjectCode(subjectCode):
    for code in subjectCode:
        print(code)

def showCourseName(CoureName):
    for name in CoureName:
        print(name) 

subjectcodelist =[]
coursename = []
with open("semester3.csv") as filecsv:
    readCSV = csv.reader(filecsv)
    for row in readCSV:
        subjectcodelist.append(row[0])
        coursename.append(row[1])

showSubjectCode(subjectcodelist)
showCourseName(coursename)
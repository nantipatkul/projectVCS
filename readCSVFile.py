import csv

def showCode(codelist):
    for data in codelist:
        print(data)

<<<<<<< HEAD
datalist = []
with open("semester2.csv") as filecsv:
    readCSV = csv.reader(filecsv)
    for row in readCSV:
        datalist.append(row[0])

showCode(datalist)
=======
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
>>>>>>> parent of 7d9dc46... Version 4.0.0

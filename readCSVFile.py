import csv

def showSubjectCode(subjectCode):
    print(subjectCode)

<<<<<<< HEAD
with open("semester3.csv") as filecsv:
    readCSV = csv.reader(filecsv)
    for row in readCSV:
        showSubjectCode(row[0])
=======
def showCourseName(coureName):
    for name in coureName:
        print(name) 

def showGrade(gradeList):
    for grade in gradeList:
        print(grade) 

subjectcodelist =[]
coursename = []
gradelist =[]
with open("semester3.csv") as filecsv:
    readCSV = csv.reader(filecsv)
    for row in readCSV:
        subjectcodelist.append(row[0])
        coursename.append(row[1])
        gradelist.append(row[2])

showSubjectCode(subjectcodelist)
showCourseName(coursename)
showGrade(gradelist)
>>>>>>> parent of 78f8444... Revert "Version 4.0.0"

import pandas as pd

def showCode(codelist):
    for data in codelist:
        print(data)

def showCourseName(CoureName):
    for name in CoureName:
        print(name) 

subjectcodelist =[]
coursename = []

data = pd.read_csv('semester2.csv')

print(data)



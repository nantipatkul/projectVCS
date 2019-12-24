import pandas as pd
import os

def showCode(codelist):
    for data in codelist:
        print(data)

def showCourseName(CoureName):  
    print(CoureName)

subjectcodelist =[]
coursename = []

data = pd.read_csv('semester3.csv')
df = pd.DataFrame(data)
print(df)

with open('log/output.txt') as target:
    target.write(df)
os.startfile('log/output1.txt')


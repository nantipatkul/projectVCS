import csv
def gradeToScore(grade):
    score = 0
    if(grade.upper() == "A"):
        score = 4
    elif(grade.upper() == "B+"):
        score = 3.5
    elif(grade.upper() == "B"):
        score = 3   
    elif(grade.upper() == "C+"):
        score = 2.5    
    elif(grade.upper() == "C"):
        score = 2
    elif(grade.upper() == "D+"):
        score = 1.5    
    elif(grade.upper() == "D"):
        score = 1    
    elif(grade.upper() == "F"):
        score = 0  
    else:
        score = -1
    gradeAfter = grade

    return score,gradeAfter

def calculaterGrade(grade,weight):  
    total = 0
    i=0 
    x=0
    for i in range(len(grade)):
        if int(grade[i])>=0:
            total = total+(float(grade[i])*int(weight[i]))
            x = x+1
    
    gpa = float(total/x)
    return gpa
        

with open('semester2.csv') as semester:
    readCSV = csv.reader(semester)
    weight = []
    gradestr =[]
    grade=[]
    for row in readCSV:
        score = row[2]
        weightSubj = row[3]
        getGrade , getGradestr = gradeToScore(score)
        grade.append(getGrade)
        gradestr.append(getGradestr)
        weight.append(weightSubj)

for i in range(len(grade)):
    
    if int(grade[i])>=0:
        print( "เกรด", grade[i] , "หน่วยกิต",weight[i])
    else:
        print( "เกรด",gradestr[i] , "หน่วยกิต",weight[i])
x = calculaterGrade(grade,weight)
print("เกรดเฉลี่ย : ",x)      
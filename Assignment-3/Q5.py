import time

with open ('q4_and_q5.txt','r') as file:
    data=file.readlines()
    for i in range(len(data)):
        data[i]=data[i].split(',')

for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j]=int(data[i][j])

courseName=input('Enter Course Number: ')
credits=int(input('Enter Credits: '))
assessments=[("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
grades={'A':80,'B':65,'C':50,'D':40}
stuDict={}
totals=[]
print()

def courseSummary(stuDict):
    global courseName
    global credits
    global assessments
    global grades
    print('\t Course Summary')
    print('\t----------------')
    print('Course Name:',courseName)
    print('Course Credits:',credits)
    print('Course Elements:',assessments)
    print('Grading:',grades)

    gradeCount={'A':0,'B':0,'C':0,'D':0,'F':0}
    for name in stuDict:
        grade=stuDict[name][2]
        gradeCount[grade]+=1

    print('Grading Summary:',gradeCount)

def printGrades(stuDict):
    print('+--------+-----------+-----+')
    print('|Roll No.|Total Marks|Grade|')
    print('+--------+-----------+-----+')
    for roll in stuDict:
        print('|'+str(roll),'|   ',stuDict[roll][1],'    | ',stuDict[roll][2],' |')
    print('+--------+-----------+-----+')
    print()

    print()
    with open('q5_grades.txt','w') as file:
        for roll in stuDict:
            file.write(str(roll)+', '+str(stuDict[roll][1])+', '+stuDict[roll][2]+'\n')
        print('Data has been written in q5_grades.txt')

def searchRecord(rollNo,stuDict):
    if rollNo in stuDict:
        print('Student Record:')
        print('---------------')
        print('Roll No:',rollNo)
        marks=[
            ("labs",stuDict[rollNo][0][0]),
            ("midsem",stuDict[rollNo][0][1]),
            ("assignments",stuDict[rollNo][0][2]),
            ("endsem",stuDict[rollNo][0][3])
            ]
        print('Marks in each assessment:',marks)
        print('Total Marks:',stuDict[rollNo][1])
        print('Grade:',stuDict[rollNo][2])
    else:
        print('Roll No. not found')

for record in data:
    stuDict[record[0]]=[record[1:]]
    stuDict[record[0]].append(sum(record[1:]))
    totals.append(sum(record[1:]))

for grade in grades:
    cutoffList=[]
    for total in totals:
        if (grades[grade]-2)<=total<=(grades[grade]+2):
            cutoffList.append(total)

    if len(cutoffList)>1:
        differencesList=[]
        cutoffList.sort()
        for i in range(len(cutoffList)-1):
            differencesList.append(cutoffList[i+1]-cutoffList[i])

        maxIndex=differencesList.index(max(differencesList))
        grades[grade]=(cutoffList[maxIndex+1]+cutoffList[maxIndex])/2

for student in stuDict:
        total=stuDict[student][1]
        if total<list(grades.values())[-1]:
            stuDict[student].append('F')
        else:
            for grade in grades:
                if total>=grades[grade]:
                    stuDict[student].append(grade)
                    break

# the following code block was used for Ques 6 grading operation time
'''
start=time.time()
for i in range(2500):
    for student in stuDict:
        total=stuDict[student][1]
        if total<list(grades.values())[-1]:
            stuDict[student].append('F')
        else:
            for grade in grades:
                if total>=grades[grade]:
                    stuDict[student].append(grade)
                    break
end=time.time()
print('Execution Time for grading operation:',end-start)
'''

while True:
    print('1) Course Summary')
    print('2) Print Grades of all Students')
    print("3) Search for a Student's Record")
    print('4) Exit')
    print()
    choice=int(input('Enter Choice: '))
    print()

    if choice==1:
        courseSummary(stuDict)
        print()

    elif choice==2:
        printGrades(stuDict)
        print()

    elif choice==3:
        rollNo=int(input('Enter Roll No. to be searched: '))
        print()
        searchRecord(rollNo,stuDict)
        print()

        # the following code block was used for Ques 6 searching operation time
        '''
        start=time.time()
        searchRecord(rollNo,stuDict)
        end=time.time()
        print('Execution Time for searching operation:',end-start)
        '''

    elif choice==4:
        print('End!')
        break

    else:
        print('Invalid Input')
        print()
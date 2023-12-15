import time

with open ('q4_and_q5.txt','r') as file:
    data=file.readlines()
    for i in range(len(data)):
        data[i]=data[i].split(',')

for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j]=int(data[i][j])

class Course:

    def __init__(self,name,credits):
        self.courseName=name
        self.credits=credits
        self.assessments=[("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
        self.grades={'A':80,'B':65,'C':50,'D':40}

    def calculateCutoff(self,totalMarksList):
        for grade in self.grades:

            cutoffList=[]
            for total in totalMarksList:
                if (self.grades[grade]-2)<=total<=(self.grades[grade]+2):
                    cutoffList.append(total)

            if len(cutoffList)>1:
                differencesList=[]
                cutoffList.sort()
                for i in range(len(cutoffList)-1):
                    differencesList.append(cutoffList[i+1]-cutoffList[i])

                maxIndex=differencesList.index(max(differencesList))
                self.grades[grade]=(cutoffList[maxIndex+1]+cutoffList[maxIndex])/2

    def courseSummary(self,stuDict):
        print('\t Course Summary')
        print('\t----------------')
        print('Course Name:',self.courseName)
        print('Course Credits:',self.credits)
        print('Course Elements:',self.assessments)
        print('Grading:',self.grades)

        gradeCount={'A':0,'B':0,'C':0,'D':0,'F':0}
        for name in stuDict:
            grade=stuDict[name][2]
            gradeCount[grade]+=1

        print('Grading Summary:',gradeCount)

class Student:

    def __init__(self):
        self.stuDict={}
        self.totals=[]  # to be used in Course.calculateCutoff

    def addRecord(self,roll,marksList):
        self.stuDict[roll]=[marksList]
        self.stuDict[roll].append(sum(marksList))
        self.totals.append(sum(marksList))

    def grading(self,grades,gradeDict):
        for student in self.stuDict:

            total=self.stuDict[student][1]
            if total<list(gradeDict.values())[-1]:
                self.stuDict[student].append('F')
            else:
                for grade in grades:
                    if total>=grades[grade]:
                        self.stuDict[student].append(grade)
                        break

    def printGrades(self):
        print('+--------+-----------+-----+')
        print('|Roll No.|Total Marks|Grade|')
        print('+--------+-----------+-----+')
        for roll in self.stuDict:
            print('|'+str(roll),'|   ',self.stuDict[roll][1],'    | ',self.stuDict[roll][2],' |')
        print('+--------+-----------+-----+')
        print()

        with open('q4_grades.txt','w') as file:
            for roll in self.stuDict:
                file.write(str(roll)+', '+str(self.stuDict[roll][1])+', '+self.stuDict[roll][2]+'\n')
        print('Data has been written in q4_grades.txt')

    def searchRecord(self,roll):
        if roll in self.stuDict:
            print('Student Record:')
            print('---------------')
            print('Roll No:',roll)
            marks=[
                ("labs",self.stuDict[roll][0][0]),
                ("midsem",self.stuDict[roll][0][1]),
                ("assignments",self.stuDict[roll][0][2]),
                ("endsem",self.stuDict[roll][0][3])
                ]
            print('Marks in each assessment:',marks)
            print('Total Marks:',self.stuDict[roll][1])
            print('Grade:',self.stuDict[roll][2])
        else:
            print('Roll No. not found')

student=Student()
course=Course(input('Enter Course Name: '),int(input('Enter Credits: ')))

for record in data:
    student.addRecord(record[0],record[1:])

course.calculateCutoff(student.totals)

student.grading(course.grades,course.grades)

# the following code block was used for Ques 6 grading operation time
'''
start=time.time()
for i in range(2500):
    student.grading(course.grades,course.grades)
end=time.time()
print('Execution Time for grading operation:',end-start)
'''

print()
while True:
    print('1) Course Summary')
    print('2) Print Grades of all Students')
    print("3) Search for a Student's Record")
    print('4) Exit')
    print()
    choice=int(input('Enter Choice: '))
    print()

    if choice==1:
        course.courseSummary(student.stuDict)
        print()

    elif choice==2:
        student.printGrades()
        print()

    elif choice==3:
        rollNo=int(input('Enter Roll No. to be searched: '))
        print()
        student.searchRecord(rollNo)
        print()

        # the following code block was used for Ques 6 searching operation time
        '''
        start=time.time()
        student.searchRecord(rollNo)
        end=time.time()
        print('Execution Time for searching operation:',end-start)
        '''

    elif choice==4:
        print('End!')
        break

    else:
        print('Invalid Input')
        print()
data={}

# creating this function to compare times since inbuilt libraries are not allowed
def timeFunc(time):
    time=list(map(int,time.split(':')))
    totalTime=(time[0]*3600)+(time[1]*60)+(time[2])
    return totalTime

with open ('q2.txt','r') as file:
    columns=file.readline().strip('\n').split(',')
    while True:
        record=file.readline().strip('\n').split(',')
        if record!=['']:
            recordDict={'crossing':record[1].strip(),'gate':record[2].strip(),'time':record[3].strip()}
            if record[0] not in data:
                data[record[0]]=[recordDict]
            else:       # handling the given special cases
                if (recordDict['crossing']=='ENTER') and (data[record[0]][-1]['crossing'])=='ENTER':
                    pass
                elif (recordDict['crossing']=='EXIT') and (data[record[0]][-1]['crossing'])=='EXIT':
                    data[record[0]][-1]=recordDict
                else:
                    data[record[0]].append(recordDict)
        else:
            break

def choice1():
    global data
    name=input('Enter Name: ').lower().title()
    if name in data:
        currentTime=timeFunc(input('Enter Time (hh:mm:ss in 24hr format): '))
        for i in range(len(data[name])):
            if timeFunc(data[name][i]['time'])>currentTime:
                if data[name][i-1]['crossing']=='ENTER':
                    print('The student is in campus right now.')
                else:
                    print('The student in not in campus right now.')
                break

        with open ('q2_out.txt','w') as file:
            file.write('Data of '+name.lower().title()+' for the day:'+'\n[\n')
            for record in data[name]:
                newTuple=(record['crossing'],record['gate'],record['time'])
                file.write(str(newTuple)+',\n')
            file.write(']')
            print('Data has been written in q2_out.txt')

    else:
        print('Student name not found')

def choice2():
    global data
    start=timeFunc(input('Enter Starting Time (hh:mm:ss in 24hr format): '))
    end=timeFunc(input('Enter End Time (hh:mm:ss in 24hr format): '))

    with open ('q2_out.txt','w') as file:
        for name in data:
            for record in data[name]:
                if timeFunc(record['time'])>end:
                    break
                if timeFunc(record['time'])>=start:
                    file.write(name+': '+str(record)+'\n')
        print('Data has been written in q2_out.txt')

def choice3():
    global data
    gateNo=input('Enter Gate Number: ')
    entryCount=0
    exitCount=0

    for name in data:
        for record in data[name]:
            if record['gate']==gateNo and record['crossing']=='ENTER':
                entryCount+=1
            elif record['gate']==gateNo and record['crossing']=='EXIT':
                exitCount+=1
    print('Number of times gate',gateNo,'was used to enter =',entryCount)
    print('Number of times gate',gateNo,'was used to exit =',exitCount)

while True:
    print('1) Student Details')
    print('2) Crossings in a given time range')
    print('3) Gate Details')
    print('4) Exit')
    print()
    choice=int(input('Enter Choice: '))
    print()

    if choice==1:
        choice1()
        print()
    
    elif choice==2:
        choice2()
        print()

    elif choice==3:
        choice3()
        print()

    elif choice==4:
        print('End')
        break
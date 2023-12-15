# the input format consists of n*(n-1) lines. n represents the number of students
# first line for each name is of format "name:"
# under each "name:" are n-1 lines representing the signatures received by the student
# these n-1 lines are of format "name, 1" or "name, 0"

try:
    with open ('q3.txt','r') as file:
        data=file.readlines()

    for i in range(len(data)):  # removing new line character
        data[i]=data[i].rstrip('\n')

    dictionary={}

    count=0
    for i in data:     # loop to find number of people
        if i[-1]==':':
            dictionary[i.rstrip(':')]=0
            count+=1

    keys=list(dictionary.keys())
    iterations=0
    low=1           # lower range for the signs of name1
    high=count      # upper range for the signs of name1

    while iterations<count:     # loop to find count for each name
        for i in range(low,high):
            if data[i][-1]=='1':
                dictionary[keys[iterations]]+=1
        iterations+=1
        low+=count
        high+=count

    values=list(dictionary.values())

    for i in range(len(values)):    # sort values in asc order
        for j in range(len(values)):
            if values[i]>values[j]:
                values[i],values[j]=values[j],values[i]
                keys[i],keys[j]=keys[j],keys[i]     # sort keys using same operations
                                                    # so indices won't change
    max,min=max(values),min(values)

    print('People with most signatures ('+str(max)+'):')
    for i in range(len(values)):
        if values[i]==max:
            print(keys[i],end=',')
    print()

    print('People with least signatures ('+str(min)+'):')
    for i in range(len(values)):
        if values[i]==min:
            print(keys[i],end=',')
except:
    print("File doesn't exist")
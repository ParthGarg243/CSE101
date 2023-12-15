# the input format is "name, marks1, marks2, ...."
# there are 7 elements in the course according to this program
# the elements' max marks and weightage are shown in the 'wts' list below

wts=[(10,5),(20,5),(100,15),(40,10),(50,25),(50,25),(80,15)]

grades={
    'A':[80,101],
    'A-':[70,80],
    'B':[60,70],
    'B-':[50,60],
    'C':[40,50],
    'C-':[35,40],
    'D':[30,35],
    'F':[0,30]
    }

try:
    with open ('q6.txt','r') as file:
        read_data=file.readlines()

    data=[]
    for i in range(len(read_data)):
        data.append(eval('['+read_data[i]+']'))     # converting str inputs to list

    final=[]

    for i in data:
        stu=[]
        stu.append(i[0])        # append roll number
        ans=True    # to check if number of student's assessments match number of actual assessments

        if len(i)!=len(wts)+1:
            ans=False           # 'ans' check failed, goes to line 58
        
        if ans:                 # find total and grade, 'ans' check successful 
            new_ans=True        # to check if marks scored in element > max marks of element
            total=0
            
            for j in range(1,len(wts)+1):   # to calculate total
                if i[j]>wts[j-1][0]:        # 'new_ans' check failed, goes to line 55
                    new_ans=False
                else:           # add marks to total
                    total+=(i[j]/wts[j-1][0])*wts[j-1][1]
            
            if new_ans:     
                stu.append(total)           # total appended, 'new_ans' check successful

                for grade in grades:        # find grade for total 
                    if total>=grades[grade][0] and total<grades[grade][1]:
                        stu.append(grade)
                        final.append(stu)
                        break

            else:
                msg="(marks scored > max marks)"
                final.append('Error! '+msg)
        else:
            msg="(number of student's assessments don't match number of actual assessments)"
            final.append("Error! "+msg)

    print('IP Results:')
    print('-----------')
    for i in final:
        print(i)
    print()

    write_data=[]
    for i in final:
        write_data.append(str(i)+"\n")

    with open ('q6_IPgrades.txt','w') as file:
            file.writelines(write_data)
    print('Data has been written in text file')

except:
    print("File doesn't exist")
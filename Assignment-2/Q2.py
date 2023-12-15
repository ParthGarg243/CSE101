def name_checker(name):
    count=0     # to divide name in two parts: name, number
    ans=False
    for i in name:
        if i.isalpha():
            count+=1
        else:
            break
    check=[name[0:count],name[count:]]
    if check[0].isupper():      # check validity of course name
        ans=True
        if check[1].isnumeric()!=True:
            ans=False
    return ans

grade_dict={
    'A+':10,
    'A':10,
    'A-':9,
    'B':8,
    'B-':7,
    'C':6,
    'C-':5,
    'D':4,
    'F':2
}

course_list=[]
inp_str='Enter Course No., Credits and Grade (separated by space): '
course=list(map(str,input(inp_str).split()))

while course!=[]:
    if name_checker(course[0]):
        if int(course[1]) in [1,2,4]:
            if course[2] in grade_dict:
                course_list.append(course)
            else:
                print('Incorrect Grade')
        else:
            print('Incorrect Credits')
    else:
        print('Improper Course Number')
    course=list(map(str,input(inp_str).split()))

course_list.sort()

numerator=0
denominator=0

for i in course_list:
    numerator+=int(i[1])*(grade_dict[i[2]])
    denominator+=int(i[1])

print()
print('\t Semester Transcript')
print('\t---------------------')

for i in course_list:
    print(i[0]+':',i[2])

print()
print('SGPA:',round(numerator/denominator,2))
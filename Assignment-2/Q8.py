# same text file format as given in the assignment

# explanation (IMP! don't forget):
# for each url, find what other urls it is referred in. the overall importance of 
# the url is sum of
# (importance of the url it is referred in)/(number of unique urls referred in that ref_url)

try:
    with open ('q8.txt','r') as File:
        data=File.readlines()

    new_dict={}

    for i in data:      # url, importance and the unique urls it refers to 
        new_dict[i[0:5]]=[float(i[7:10])]
        low=5
        high=8
        while high<=len(i):     # finds the unique urls
            if i[low:high]=='URL' and i[high:high+2].isdigit():
                if i[low:high+2] not in new_dict[i[0:5]]:
                    new_dict[i[0:5]].append(i[low:high+2])
            low+=1
            high+=1

    ans_dict={}

    for url in list(new_dict.keys()):   # finds overall importance of each url
        importance=0
        for ref_url in list(new_dict.keys()):
            if (url!=ref_url) and (url in new_dict[ref_url]):
                importance+=(new_dict[ref_url][0])/(len(new_dict[ref_url])-1)
        ans_dict[url]=importance

    keys=list(ans_dict.keys())
    values=list(ans_dict.values())

    for i in range(len(keys)):      # sorting according to overall importance
        for j in range(len(keys)):
            if values[i]>values[j]:
                values[i],values[j]=values[j],values[i]
                keys[i],keys[j]=keys[j],keys[i]

    n=int(input('How many top ranked pages do you want to see: '))
    if n>len(keys):
        print('Only',len(keys),'pages exist: ')
        for i in range(len(keys)):
            print(keys[i]+':',values[i])
    else:
        print('Top',n,'ranked pages: ')
        for i in range(n):
            print(keys[i]+':',values[i])
except:
    print("File doesn't exist")
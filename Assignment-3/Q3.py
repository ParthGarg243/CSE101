# text in txt files generated using dummytextgenerator.com

import random

with open ('q3_scores.txt','w'):    # creating the file to write in it later, line #78
    pass

files=['q3_File1.txt','q3_File2.txt','q3_File3.txt','q3_File4.txt']

def f1_calc(uniques,total):
    f1=len(uniques)/len(total)
    return f1

def f2_calc(countList,total):
    f2=sum(countList)/len(total)
    return f2

def f3_calc(sentences):
    f3=0
    for sentence in sentences:
        if 5<len(sentence.split())<35:
            f3+=1
    return f3/len(sentences)

def f4_calc(count,total):
    f4=count/len(total)
    return f4

def f5_calc(total):
    if len(total)>750:
        return 1
    else:
        return 0

for fileName in files:
    try:
        with open (fileName,'r') as file:
            data=file.read()
            sentences=[i.strip() for i in data.split('.') if i!='']
            
            f3=f3_calc(sentences)

            total=[]
            uniques=[]
            for sentence in sentences:
                for word in sentence.split():
                    total.append(word.lower().strip(','))
                    if word not in uniques:
                        uniques.append(word.lower().strip(','))
            
            f1=f1_calc(uniques,total)
            f5=f5_calc(total)

            wordCount={}
            for word in uniques:
                wordCount[word]=total.count(word)

            countList=list(wordCount.values())
            wordList=list(wordCount.keys())

            for i in range(len(countList)):
                for j in range(len(countList)):
                    if countList[i]>countList[j]:
                        countList[i],countList[j]=countList[j],countList[i]
                        wordList[i],wordList[j]=wordList[j],wordList[i]

            f2=f2_calc(countList[-5:],total)

            count=0
            for character in data:
                if character in [';',':',',','.']:
                    count+=1

            f4=f4_calc(count,total)

            score=4+(f1*6)+(f2*6)-f3-f4-f5

            with open('q3_scores.txt','a') as file:
                file.write(fileName+'\n')
                file.write('score: '+str(round(score,2))+'\n')
                file.write('5 most used words in decreasing order: ' + str(wordList[-5:][::-1]) + '\n')
                new=random.sample(uniques,5)
                file.write('5 random words from the file: ' + str(new) + '\n')
    except:
        print('File',fileName,"doesn't exist.")

print('Check q3_scores.txt file')
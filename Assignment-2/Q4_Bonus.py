import pip._vendor.requests as requests
from random import randint

api_url='https://api.dictionaryapi.dev/api/v2/entries/en/'

pc=['_','_','_','_','_']
lc=[]

def position_checker(guess,word):       # letter in word, correct position
    global pc
    global lc
    for i in range(5):
        if guess[i]==word[i]:
            pc[i]=guess[i]
    return ''.join(pc)

def letter_checker(guess,word):         # letter in word, wrong position
    global pc
    global lc    
    for i in range(5):
        if guess[i] in word and guess[i]!=word[i]:
            if (pc.count(guess[i])+lc.count(guess[i]))<word.count(guess[i]):
                lc.append(guess[i])
    if len(lc)>0:
        return lc
    else:
        return None

word_list=[
    'blade','stand','array','bloom','bowel','speed','peace','flock','trust','lodge',
    'minor','drink','equal','pitch','thumb','think','salad','opera','judge','troop',
    'faint','queue','upset','worth','lover','spend','sweep','creep','truck','hello',
    'tempt','organ','coach','merit','refer','order','green','crime','spell','embox',
    'guess','force','marsh','split','cause','chase','party','venus','agile','aisle',
    'exact','flush','allow','march','trend','shift','spill','chest','swing','straw',
    'ratio','ghost','cross','throw','sharp','berry','voice','motif','carry','start',
    'small','wheat','shout','visit','scene','pound','final','novel','ditch','sound',
    'bland','wound','onion','shoot','grain','smell','glory','skate','uncle','stall',
    'reign','scrap','horse','loose','shine','dirty','aware','bingo','glove','scarf'
]

word=word_list[randint(0,99)]

i=0
ans=False

while i<=6:
    guess=input('Enter a five letter word: ')
    if len(guess)==5:
        
        new_url=api_url+guess
        resp=requests.get(new_url)
        
        if resp.status_code==200:   # successful call (a valid english word)
            i+=1
            pc=['_','_','_','_','_']
            lc=[]
            if guess==word:
                ans=True
                break
            else:
                print('Letters in the correct place:',position_checker(guess, word))
                print('Letters in the word but not in the correct place:',letter_checker(guess,word))
        else:                       # failed call (word not found in online dictionary)
            print('Please enter a valid english word')
    else:
        print('Invalid Input')

if ans:
    print('Congrats! You guessed the word in',str(i),'tries')
else:
    print('Oops! No more tries left')
    print('The word was',word)
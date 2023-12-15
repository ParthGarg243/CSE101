ones=[
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

ten_teens=[
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
]

tens=[
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
]

more=[
    'crore',
    'lakh',
    'thousand',
]

def digits_2(n):
    if len(str(n))==1:          # len=1 
        return ones[n]
    elif len(str(n))==2:        # len=2
        if 10<=n<=19:           # ten or teens
            index=n-10
            return ten_teens[index]
        elif (str(n))[-1]=='0': # multiple of ten
            index=(n//10)-2
            return tens[index]
        else:                   # len=2, not multiple of ten   
            tens_index=(n//10)-2
            ones_index=n%10
            return tens[tens_index]+' '+ones[ones_index]

def digits_3(n):              # len=3
    if (str(n))[-2::]=='00':  # multiple of hundred
        index=n//100
        return ones[index]+' hundred'
    else:                     # len=3, not multiple of hundred
        index1=n//100
        index2=n%100
        return ones[index1]+' hundred and '+digits_2(index2)

def naming_func(n): 
    naming=[]
    name=''
    div=10000000
    
    for i in range(3):    # Cr, Lkh and Th parts of name 
        if n//div!=0:
            naming.append(int(n//div))
        else:
            naming.append(None)  
        n=int(n%div)
        div=div/100
    
    for i in range(len(naming)):    # parts of name > 999
        if naming[i]!=None:
            name+=digits_2(naming[i])+' '+more[i]+' '
    
    if n!=0:                        # parts of name < 1000
        if len(str(n))==3:
            name+=digits_3(n)
        elif len(str(n))<3:
            name+=digits_2(n)
    return name

num=int(input('Enter Number: '))
if len(str(num))<3:
    print(digits_2(num))
else:
    print(naming_func(num))
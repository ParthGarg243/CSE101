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

n=int(input('Enter Number: '))

if len(str(n))==1:          # ones 
    print(ones[n])
elif len(str(n))==2:
    if 10<=n<=19:           # tens + teens
        index=n-10
        print(ten_teens[index])
    elif (str(n))[-1]=='0': # multiple of ten
        index=(n//10)-2
        print(tens[index])
    else:                   # len=2, not multiple of ten   
        tens_index=(n//10)-2
        ones_index=n%10
        print(tens[tens_index],ones[ones_index])
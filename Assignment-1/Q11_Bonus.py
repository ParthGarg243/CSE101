'''
Q) Write a menu driven program to convert a number in decimal system 
   to either binary or octal or hexadecimal system according to the 
   user's choice. Take the number as input from the user and which 
   system should the number be converted to   
'''

binary=''
octal=''
hexadecimal=''

def decimal_to_binary(n):   
    if n>=1:
        global binary
        binary+=str(n%2)
        decimal_to_binary(n//2)

def decimal_to_octal(n):
    if n>=1:
        global octal
        octal+=str(n%8)
        decimal_to_octal(n//8)

def decimal_to_hexadecimal(n):
    if n>=1:
        global hexadecimal
        if n%16<10:
            hexadecimal+=str(n%16)
        elif n%16==10:
            hexadecimal+='A'
        elif n%16==11:
            hexadecimal+='B'
        elif n%16==12:
            hexadecimal+='C'
        elif n%16==13:
            hexadecimal+='D'
        elif n%16==14:
            hexadecimal+='E'
        elif n%16==15:
            hexadecimal+='F'
        decimal_to_hexadecimal(n//16)

while True:
    print('\t\tNumber System Conversions')
    print('1) Decimal to Binary')
    print('2) Decimal to Octal')
    print('3) Decimal to Hexadecimal')
    print('4) Exit')
    print()
    choice=int(input('Enter Choice:'))
    print()

    if choice==1:
        print('\tDecimal to Binary')
        binary=''
        num=int(input('Enter Number:'))
        if num==0:
            print(num,'in binary system =',num)        
        else:
            decimal_to_binary(num)
            print(num,'in binary system =',binary[::-1])
        print()

    elif choice==2:
        print('\tDecimal to Octal')
        octal=''
        num=int(input('Enter Number:'))
        if num==0:
            print(num,'in octal system =',num)        
        else:
            decimal_to_octal(num)
            print(num,'in octal system =',octal[::-1])
        print()

    elif choice==3:
        print('\tDecimal to Hexadecimal')
        hexadecimal=''
        num=int(input('Enter Number:'))
        if num==0:
            print(num,'in hexadecimal system =',num)        
        else:
            decimal_to_hexadecimal(num)
            print(num,'in hexadecimal system =',hexadecimal[::-1])
        print()

    elif choice==4:
        print('The End')
        break

    else:
        print('Invalid Input')
        print()
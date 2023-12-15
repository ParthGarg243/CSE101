def fact(n):
    ans=1
    if n==0:
        return ans
    else:
        for i in range(1,n+1):
            ans*=i
        return ans

def sin(deg):
    if 0<=deg<=90:
        ans=0
        i=-1
        deg*=3.14/180
        pow=1
        for j in range(25):
            ans+=(i**j)*((deg**pow)/fact(pow))
            pow+=2
        return round(ans,2)
    else:
        return 'Input out of range'

def cos(deg):
    if 0<=deg<=90:
        ans=0
        i=-1
        deg*=3.14/180
        pow=0
        for j in range(25):
            ans+=(i**j)*((deg**pow)/fact(pow))
            pow+=2
        return round(ans,2)
    else:
        return 'Input out of range'

degree=float(input('Enter angle of the view to top (in degrees): '))
base=float(input('Enter the distance to the base of pole: '))

tan=sin(degree)/cos(degree)
height=round((base*tan),2)
hypotenuse=round((base/cos(degree)),2)

print('Height of pole:',height)
print('Distance to the top of pole:',hypotenuse)
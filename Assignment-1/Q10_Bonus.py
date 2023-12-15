def func(x):
    return (x**3)-(10.5*(x**2))+(34.5*x)-35
def funcd(x):
    return (3*(x**2))-(21*x)+34.5

def newton(f,g,x):
    x=x-(f(x)/g(x))
    return x

roots=[]
n=3
x1=float(input('Enter lower limit of range:'))
x2=float(input('Enter upper limit of range:'))
x=x1
iterations=1  #to stop the prog if (no. of roots)<n in given range

while len(roots)<n:
    for i in range(100):
        iterations+=1
        if x1<=x<=x2:
            if -0.1<=func(x)<=0.1:
                if round(x,2) not in roots:
                    if round(x,2)%0.5==0:
                        roots.append(round(x,2))
        x=newton(func,funcd,x)
    if iterations>300:
        break
    x+=1

if len(roots)>0:
    print('Roots found within the given range:',roots)
else:
    print('No roots found')
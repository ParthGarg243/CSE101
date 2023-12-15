def func(x):
    return (x**3)-(10.5*(x**2))+(34.5*x)-35
def funcd(x):
    return (3*(x**2))-(21*x)+34.5

def newton(f,g,x):
    x=x-(f(x)/g(x))
    return x

x=float(input('Enter initial value of x: '))
root=0
for i in range(100):
    if -0.1<=func(x)<=0.1:
        root=round(x,2)
        break
    x=newton(func,funcd,x)
if root!=0:
    print('Root found:',round(x,2))
else:
    print('No root found for the given initial value')
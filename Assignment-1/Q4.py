import math

start=float(input('Enter Starting Time: '))
end=float(input('Enter End Time: '))

t1=(start)
t2=(start+0.25)
dist=0
while t2<=end:
    val1=(2000*(math.log(140000/(140000-(2100*t1))))) - (9.8*t1)
    val2=(2000*(math.log(140000/(140000-(2100*t2))))) - (9.8*t2)
    vel=(val1+val2)/2
    dist+=vel*(0.25)
    t1+=0.25
    t2+=0.25

print('Total Distance Traveled:',dist)
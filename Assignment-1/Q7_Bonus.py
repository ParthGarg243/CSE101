cost=int(input('Enter cost: '))             #45000,65000,125000
allowance=int(input('Enter allowance: '))   #20000
sf=float(input('Enter savings fraction: ')) #0.1
r=float(input('Enter rate of interest: '))  #0.5
savings=allowance*sf
t=0
bank=0

while bank<cost:
    bank+=savings
    bank*=(100+r)/100
    t+=1

print('Months taken:',t)
print()

time=int(input('Enter number of months less than '+str(t)+':'))
new_bank=0
new_sf=sf+0.001

while True:
    savings=allowance*new_sf
    for i in range(time):
        new_bank+=savings
        new_bank*=(100+r)/100
    if new_bank>cost:
        print('New savings fraction:',round(new_sf,3))
        break
    else:
        new_bank=0
        new_sf+=0.001
cost=int(input('Enter cost: '))             #45000,65000,125000
allowance=int(input('Enter allowance: '))   #20000
sf=float(input('Enter savings fraction: ')) #0.1
r=float(input('Enter rate of interest: '))  #0.5
savings=allowance*sf
t=0
bank=0

while bank<cost:
    bank+=savings
    bank*=((100+r)/100)
    t+=1

print('Months taken:',t)
print('Savings after buying laptop:',round(bank-cost,2))
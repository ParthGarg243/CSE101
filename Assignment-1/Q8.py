pop=list(map(int,input('Enter population of each continent separated by space: ').split()))
# [50,1450,1400,1700,1500,600,1200]
rate=2.5
rate_copy=rate
total=0
for i in pop:
    total+=i
print('Current Total Population:',total)

total2=total
n=0

while total2>=total:
    for i in range(len(pop)):
        pop[i]+=(rate_copy*pop[i])/100
        rate_copy-=0.4
    rate-=0.1
    rate_copy=rate
    total=total2
    total2=0
    for i in pop:
        total2+=i
    n+=1

print('Max population reached after '+str(n-1)+' years')
print('Max Population:',round(total,2),'millions')
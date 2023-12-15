price=1
e=2.72
def demand(price):
    return round(e**(10-(1.05*price)),2)
def supply(price):
    return round(e**(1+(1.06*price)),2)

d=demand(price)
s=supply(price)

while d-s>5:
    price=price+price*(0.005)
    d=demand(price)
    s=supply(price)

print('Equilibrium Price:',round(price,2))
print('Demand at Equilibrium:',d)
print('Supply at Equilibrium:',s)
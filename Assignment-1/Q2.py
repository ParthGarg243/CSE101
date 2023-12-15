eq1=[]  # 8x+2y=400
eq2=[]  # 2x+y=120
m_values=[0,10,20]

for x1 in range(int(400/8)+1):
    for y1 in range(int(400/2)+1):
        if (8*x1)+(2*y1)==400:
            eq1.append([x1,y1])

for x2 in range(int(120/2)+1):
    for y2 in range(120+1):
        if (2*x2)+(y2)==120:
            eq2.append([x2,y2])

for i in eq1:
    for j in eq2:
        if i[0]==j[0] and i[1]==j[1]:
            x,y=i[0],i[1]

profits=[]

for m in m_values:
    profit=0
    for i in range(1,x+1):
        if i<=m:
            profit+=90
        else:
            profit+=100
    for j in range(1,y+1):
        if j<=m:
            profit+=25
        else:
            profit+=30
    profits.append(profit)

print(profits)
print('Max profit is',max(profits),'when M =',m_values[profits.index(max(profits))])
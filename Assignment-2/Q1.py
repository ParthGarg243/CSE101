menu=[      # added spaces to fix the spacing in menu
    ("Samosa   ", 15),
    ("Idli     ", 30),
    ("Maggie   ", 50),
    ("Dosa     ", 70),
    ("Tea      ", 10),
    ("Coffee   ", 20),
    ("Sandwich ", 35),
    ("ColdDrink", 25)
]

print('    Canteen Menu')
print('   --------------')

num=1

for i in menu:
    print(str(num)+')',i[0],'\t'+str(i[1]))
    num+=1

inp_str='Enter item number and quantity (separated by space): '
items_list=[]
item=list(map(int,input(inp_str).split()))

while item!=[]:     #item[0]=item no., item[1]=quantity
    if -1<int(item[0])-1<len(menu):    # check if item no. in menu
        if len(item)==2 and str(item[1]).isnumeric():    # check quantity
            items_list.append(item)
            item=list(map(int,input(inp_str).split()))
        else:
            print('Invalid Quantity')
            item=list(map(int,input(inp_str).split()))
    else:
        print('Item not in menu')
        item=list(map(int,input(inp_str).split()))

order=[]
sum=[0,0]           # sum[0]=total items, sum[1]=total amt.

for i in items_list:
    item=[]         # item[0]=name, item[1]=cost
    item.append(menu[i[0]-1][0])
    item.append((menu[i[0]-1][1])*i[1])
    order.append(item)
    sum[0]+=i[1]
    sum[1]+=item[1]

print()
print('     Bill')
print('    ------')

num=0

for i in order:
    print(i[0].strip()+',',str(items_list[num][1])+',','Rs',i[1])
    num+=1

print()
print('TOTAL,',sum[0],'items,','Rs',sum[1])
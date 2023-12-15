# the address book is of the following format
# dictionary with keys as name and the values as a list of records with that name

try:
    with open("q7.txt","r") as file:
        data=eval(file.read())
    if data!='':
        address_book=data
    else:
        address_book={}
except:
    address_book={}

def insert_entry():
    global address_book
    name=input('Enter name: ')
    address=input('Enter address: ')
    phone=input('Enter mobile number: ')
    email=input('Enter E-Mail ID: ')
    record_dict={'address':address,'phone':phone,'email':email}
    
    if (name in address_book) and (record_dict not in address_book[name]):
        address_book[name].append(record_dict)
    else:
        address_book[name]=[record_dict]
    
    print('Entry Inserted')

def delete_entry():
    global address_book
    name=input('Enter name whose entry is to be deleted: ')
    
    if name in address_book:
        del address_book[name]
        print('Entry deleted')
    else:
        print('Entry not found')

def search_name():
    global address_book
    name=input('Enter name whose entry is to be searched: ')
    results=[]
    
    for i in address_book:
        if name in i:
            for result in address_book[i]:
                results.append([name,result])

    if len(results)>0:
        print('Results found:')
        for i in results:
            print(i[0]+':',i[1])
    else:
        print('No result found')

def search_phone():
    global address_book
    phone=input('Enter phone number whose entry is to be searched: ')
    results=[]
    
    for name in address_book:
        for entry in address_book[name]:
            if entry['phone']==phone:
                results.append([name,entry])
    
    if len(results)>0:
        print('Results found:')
        for i in results:
            print(i[0]+':',i[1])
    else:
        print('No result found')

def search_email():
    global address_book
    email=input('Enter Email ID whose entry is to be searched: ')
    results=[]
    
    for name in address_book:
        for entry in address_book[name]:
            if entry['email']==email:
                results.append([name,entry])
    
    if len(results)>0:
        print('Results found:')
        for i in results:
            print(i[0]+':',i[1])
    else:
        print('No result found')

while True:
    print('\t Address Book')
    print('\t--------------')
    print('1) Insert an Entry')
    print('2) Delete an Entry')
    print('3) Search for Entries using name')
    print('4) Search for Entry using phone number')
    print('5) Search for Entry using email')
    print('6) Exit')
    print()
    choice=int(input('Enter Choice: '))
    print()
    if choice==1:
        insert_entry()
        print()
    elif choice==2:
        delete_entry()
        print()
    elif choice==3:
        search_name()
        print()
    elif choice==4:
        search_phone()
        print()
    elif choice==5:
        search_email()
        print()
    elif choice==6:
        print('The End')
        break
    else:
        print('Invalid Choice')
        print()

with open("q7.txt","w") as file:
    file.write(str(address_book))
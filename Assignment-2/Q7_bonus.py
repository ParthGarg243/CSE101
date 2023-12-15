try:
    with open ("q7_bonus_friendFile.txt","r") as file:
        myBook=eval(file.read())

    try:
        with open("q7_bonus_myFile.txt","r") as file:
            friendBook=eval(file.read())

        for name in friendBook:
            if name in myBook:
                for record in friendBook[name]:
                    if record not in myBook[name]:
                        myBook[name].append(record)
            else:
                myBook[name]=friendBook[name]

        print('Merged Address Book:')
        for name in myBook:
            print(name+':')
            for record in myBook[name]:
                print(record)
    except:
        print("File doesn't exist")
except:
    print("File doesn't exist")
from Entry import *
import datetime

LOOK_UP=1
ADD=2
CHANGE=3
DELETE=4
SHOWALL=5
QUIT=6

FILENAME="Note.csv"

def main():
    inicil()
    mycontacts=load_contacts()
    

    choice=0
    
   
    while choice!=QUIT:

        choice=get_menu_choice()
        

        if choice==LOOK_UP:
            look_up(mycontacts)
        elif choice==ADD:
            add(mycontacts)
        elif choice==CHANGE:
            change(mycontacts)
        elif choice==DELETE:
            delete(mycontacts)
        elif choice==SHOWALL:
            showall(mycontacts)
        mycontacts=load_contacts()
            


def inicil():
    try:
        input_file=open(FILENAME, "w")
        input_file.close()
        
    except IOError:
        print("Eror")
        
def load_contacts():
    try:
        input_file=open(FILENAME, "r")

        contact_dct= input_file.read()
        
        input_file.close()
        
    except IOError:
        contact_dct=[]
        
    return contact_dct

def look_up(mycontacts):
    id=int(input("Введите ID:  "))
    lines = mycontacts.split('\n')
    for line in lines:
        if line is not "":
            allinf = line.split(';')
            if int(allinf[0]) is id:
                obj = Entry(allinf[0], allinf[1], allinf[2], allinf[3])
                print(obj.get_all())

def add(mycontacts):
    countid =0
    len=0
    lines = mycontacts.split('\n')
    for line in lines:
            len+=1
    for item in range(len):
        for line in lines:
            if line is not "":
                allinf = line.split(';')
                if int(allinf[0]) is countid:
                    countid+=1

    id=countid
    head=input("Заголовок: ")
    body=input("Тело заметки: ")
    data=datetime.datetime.now().time()
    
    entr = Entry(id, head, body, data)
    addfile(entr)


def addfile(entry):
    try:
        input_file=open(FILENAME, "a")

        contact_dct= input_file.write(entry.get_allf())
        
        input_file.close()
        
    except IOError:
        contact_dct=[]

def change(mycontacts):
    # get a name to look up.
    id=int(input("Введите ID: "))
    lines = mycontacts.split('\n')
    for line in lines:
        if line is not "":
            allinf = line.split(';')
            if int(allinf[0]) is id:
                deletefile(id,mycontacts)
                idn=allinf[0]
                head=input("Заголовок: ")
                body=input("Тело заметки: ")
                data=datetime.datetime.now().time()
                ent = Entry(idn, head, body, data)
                addfile(ent)


def delete(mycontacts):
    id=int(input("Введите ID: "))
    lines = mycontacts.split('\n')
    for line in lines:
        if line is not "":
            allinf = line.split(';')
            if int(allinf[0]) is id:
                deletefile(id,mycontacts)

def deletefile(id,mycontacts):
    mycontacts2=""
    lines = mycontacts.split('\n')
    for line in lines:
        if line is not "":
            allinf = line.split(';')
            if int(allinf[0]) is not id:
                mycontacts2 += line +"\n"
    savefile(mycontacts2)
    
def savefile(mycontacts):
    try:
        input_file=open(FILENAME, "w")

        contact_dct= input_file.write(mycontacts)
        
        input_file.close()
        
    except IOError:
        contact_dct=[]

def showall(mycontacts):
    lines = mycontacts.split('\n')
    for line in lines:
        if line is not "":
            allinf = line.split(';')
            obj = Entry(allinf[0], allinf[1], allinf[2], allinf[3])
            print(obj.get_all()+"\n-------------------------------")
        

def get_menu_choice():
    print()
    print("Menu")
    print("-------------------")
    print("1. Посмотреть заметку.")
    print("2. Добавить заметку.")
    print("3. Изменить заметку.")
    print("4. Удалить заметку.")
    print("5. Показать все заметки.")
    print("6. Выйти из программы.")
    print()

    choice=int(input("Enter your choice: "))

    while choice<LOOK_UP or choice>QUIT:
        choice=int(input("Enter a valid choice: "))

    return choice


if __name__=="__main__":
    main()
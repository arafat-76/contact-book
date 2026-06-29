import json
def save(contacts):
    f=open("contacts.txt","w")
    json.dump(contacts,f)
    f.close()
def load():
    try:
        f=open("contacts.txt","r")
        contacts=json.load(f)
        f.close()
        return contacts
    except:
        return{}
contacts=load()
while True:
    print("1.add contacts")
    print("2.show contacts")
    print("3.search contact")
    print("4.delete contact")
    print("5.quit")
    print("6.show all contacts")
    choice=input("choose:")
    if choice=="1":
        name=input("Enter name:")
        phone=input("Enter phone number:")
        contacts[name]=phone
        save(contacts)
    elif choice=="2":
        for name in contacts:
            print(name,":",contacts[name])
    elif choice=="3":
        name=input("Enter name to search:")

        if name in contacts:
            print(name,":",contacts[name])
        else:
            print("contact not found")
    elif choice=="4":
        name=input("enter name to delete")
        if name in contacts:
            del contacts[name]
            save(contacts)
            print("contact deleated")
        else:
            print("contact not found")
    elif  choice=="5":
        print("5")
        break

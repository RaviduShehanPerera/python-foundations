print("===Contact Book===")

contacts = []

while True:

    command = input("choose one of the following command : Add, search, remove, quit: ")
    command = command.lower()

    if command =="quit":
        break
    elif command =="add":
        name = input("name? ")
        phone = input("phone? ")
        email = input("email? ")

        contact = {"name":name, "phone":phone, "email":email}
        contacts.append(contact)

        print ("contact added!") 

    elif command == "remove":

        name =input("who do you want remove?  ")
        
        for contact in contacts:
            if  contact["name"].lower() == name.lower():
                contacts.remove(contact)
            print( "Deleted!")
            break
        else:
            print("No Such contact found")

    elif command == "show":
        for key,values in enumerate(contacts):
            print(f'{key+1}. {values["name"]}--{values["phone"]}--{values["email"]}')

    elif command =="search":
        name = input("who do you want to search ? ")
        for contact in contacts:
            if contact["name"].lower() == name.lower():
                print(f'Name: {contact["name"]}')
                print(f'phone:{contact["phone"]}')
                break           
            else: 
                print("No such contact found")    
print("Goodbye!")        
contacts = {}

print("Welcome to the contact book")

while True:
    add_contact = "add contact"
    print("1 :",add_contact)
    view_contact = "view contact"
    print("2 :",view_contact)
    update_contact = "update contact"
    print("3 :",update_contact)
    del_contact = "delete contact"
    print("4 :",del_contact)
    search_contact = "search contact"
    print("5 :",search_contact)
    display_contact = "display contact"
    print("6 :",display_contact)
    exit_contact = "exit_contact"
    print("7 :",exit_contact)

    user_choice = int(input("Enter a user choice :"))

    if user_choice == 1:
       name = input("Enter the contact name :")
       if name not in contacts:
           phone = int(input("Enter a phone number :"))
           email = input("Enter email id :")
           address = input("Enter an address :")
           contacts[name] = {'phone':phone,'email':email,'address':address}
           print("Contact name {} created successfully ".format(name))
       else:
           print("Conatct name already exists {}".format(name))

    elif user_choice == 2:
       name = input("Enter a contact name to view :")
       if name in contacts:
           contact = contacts[name]
           details = "Name : {0} , Phone number : {1} , Email-id : {2} , Address : {3}"
           print(details.format(name,phone,email,address))
       else:
           print("Contact name has not found")

    elif user_choice == 3:
       name = input("Enter a contact name to update :")
       if name not in contacts:
           print("Contact not found with that name")
       else:
           phone = int(input("Enter a updated phone number :"))
           email = input("Enter a updated email :")
           address = input("Enter a updated address :")
           details = "Name : {0} , Phone number : {1} , Email-id : {2} , Address : {3}"
           print(details.format(name,phone,email,address))
           print("Contact name {} updated successfully ".format(name))

    elif user_choice == 4:
       name = input("Enter a contact name to delete :")
       if name in contacts:
           del contacts[name]
           print("Contact name {} has been deleted successfully ".format(name))
       else:
           print("Contact not found")

    elif user_choice == 5:
       search_name = input("Enter a contact name to search :") 
       search_contact = int(input("Enter a phone number to search :"))
       for name,contact in contacts.items():
            if search_name in name :
                print('found - Name:{}, Phone number:{}, Email:{}, Address:{}'.format(name,phone,email,address))
            else:
                print("No contact found with that name and phone number")

    elif user_choice == 6:
        if contacts == {}:
            print("There are no contacts")
        else:
            print("Total contacts in contact book :",len(contacts))

    elif user_choice == 7:
        print("Thanks for using contact book")
        break 

    else:
        print("You have entered invalid input")

    
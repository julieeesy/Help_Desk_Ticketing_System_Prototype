# --------------------<< MENU MAKER >>--------------------
def menuload(menu):
    count = 1

    for z in menu:
        print(f"{count}. {z}")
        count += 1
    print(f"0. EXIT")
    choice = input("\nEnter Number: ")

    if choice.isnumeric():
        choice = int(choice)

        # checks and returns how much options there is in the menu
        if choice in range(0, count):
            answer = choice

        else:
            print("Error: Number out of RANGE.")
            answer = 99

    else:
        print("Error: Input NOT a number.")
        answer = 99

    return answer

# --------------------<< PRINTING TICKETS --IGNORE >>--------------------
# loading the tickets
def loading_all_tickets(menu):
    count = 1
    for z in menu:
        print(f"{z}")
        count += 1
    print(f"0. Back to Main Menu")
    choice = input("\nEnter Number: ")

    if choice.isnumeric():
        choice = int(choice)

        # checks values from 0 and until where the index of the menu is counted and will return the value of choice
        if choice in range(0, count):
            answer = choice

        else:
            print("Error: Number out of RANGE.")
            answer = 99

    else:
        print("Error: Input NOT a number.")
        answer = 99

    return answer

# printing the tickets
def printing_tickets():
    found = 0
    vTemp = []

    print("\nPrinting Tickets: ")
    for v in client_list:
        if v.Status == True:
            vTemp.append(f"Ticket Number: {v.ticket_number}\n"
                         f"Ticket creator: {v.ticket_creator}\n" 
                         f"Staff ID: {v.staff_id}\n"
                         f"Email Address: {v.email}\n"
                         f"Description: {v.desc}\n"
                         f"Response: {v.response}\n"
                         f"Ticket Status: {v.ticket_status}\n")

    test = loading_all_tickets(vTemp)

    if test != 0:
        found = client_list[test - 1]

    return found

# --------------------<< HELP DESK >>--------------------
def ticket_find():
    found = 0
    print("\n------------FIND TICKET------------")
    findMenu = ["By TICKET NUMBER", "By TICKET CREATOR", "By STAFF ID"]
    selection = menuload(findMenu)

    # find the ticket by TICKET NUMBER
    if selection == 1:
        find_ticket_number = input("Enter TICKET NUMBER: ")

        if find_ticket_number.isnumeric():
            find_ticket_number = int(find_ticket_number)
            for x in client_list:
                if x.ticket_number == find_ticket_number:
                    found = x
                    print("Ticket Number Found!\n")
                    print(x)
                    break
            else:
                print("Error: Ticket Number Not Found :( \n")
                """ another way to print
            if find_ticket_number != x.ticket_number:
                print("Error: Ticket Number Not Found :( \n") 
                """

    # find the ticket by TICKET CREATOR
    elif selection == 2:
        find_ticket_creator = input("Enter TICKET CREATOR: ").lower()

        for x in client_list:
            if x.ticket_creator.lower() == find_ticket_creator:
                found = x
                print("Ticket Creator Found!\n")
                print(x)
                break
        else:
            print("Error: Ticket Creator Not Found :( \n")
        """
        if find_ticket_creator not in x.ticket_creator.lower():
            print("Error: Ticket Creator Not Found :( \n")
        """


    # find the ticket by STAFF ID
    elif selection == 3:
        find_staff_id = input("Enter STAFF ID: ")

        for y in client_list:
            if y.staff_id == find_staff_id:
                found = y
                print("Staff ID Found!\n")
                print(y)
                break
        else:
            print("Error: Staff ID Not Found :( \n")
            """
        if find_staff_id not in y.staff_id:
            print("Error: Staff ID Not Found :( \n")
            """


    elif selection == 0:
        print("Going back to main menu...")

    else:
        print("Error: Wrong Input for Finding Ticket")

    return found

def ticket_edit():
    change_ticket = ticket_find()

    if change_ticket != 0:
        edit_menu = ["Respond to Ticket", "Change Ticket Status"]
        editPick = menuload(edit_menu)

        if editPick == 1:
            change_ticket.new_response()
            change_ticket.ticket_status = "Closed"
            print("New changes added to the Ticket!!!")

        elif editPick == 2:
            change_ticket.new_ticket_status()
            print("New changes added to Ticket Status!!!")

        elif editPick == 0:
            print("Going back to main menu...")


# --------------------<< Submit A Ticket >>--------------------
def submit_ticket():
    ticket_creator = input("ENTER Ticket creator: ")
    staff_id = input("ENTER Staff ID: ")
    email = input("ENTER Email Address: ")
    desc = input("ENTER Description: ")

    new_submit_ticket = Ticket(ticket_creator, staff_id, email, desc)
    client_list.append(new_submit_ticket)
    print("\nNew TICKET Submitted!!!\n")
    print(client_list[len(client_list) - 1]) # https://blog.gitnux.com/code/python-print-object/

# --------------------<< DISPLAY TICKET STATISTICS >>--------------------
# Function to calculate and display ticket statistics
def display_ticket_statistics():
    created_tickets = 0
    tickets_resolved = 0
    tickets_to_solve = 0

    for ticket in client_list:
        if ticket.ticket_status == "Open" or ticket.ticket_status == "Closed" or ticket.ticket_status == "closed" or ticket.ticket_status == "open":
            created_tickets += 1
            if ticket.ticket_status == "Closed" or ticket.ticket_status == "closed":
                tickets_resolved += 1
            elif ticket.ticket_status == "Open" or ticket.ticket_status == "open":
                tickets_to_solve += 1

    print("\nTicket Statistics:")
    print(f"Tickets Created: {created_tickets}")
    print(f"Tickets Resolved: {tickets_resolved}")
    print(f"Tickets To Solve: {tickets_to_solve}")



# --------------------<< CHANGING PASSWORDS IN A TICKET >>--------------------
import random
import string
# Function to check if a ticket contains a keyword related to password reset
def contains_password_reset_keyword(ticket):
    keywords = ["password reset", "forgot password", "reset my password", "password"]
    for keyword in keywords:
        if keyword in ticket.desc.lower():
            return True
    return False

# Function to generate a new password
def generate_new_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))



# --------------------<< class >>--------------------
from Tickets import Ticket

client_list = []

# --------------------<< main >>--------------------
# dummy data :>
client_data_01 = Ticket("Inna", "INNAM", "inna@whitecliffe.co.nz", "My monitor stopped working")
client_data_02 = Ticket("Maria", "MARIAH", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars")
client_data_03 = Ticket("John", "JOHNS", "john@whitecliffe.co.nz", "Password change")
client_list.extend([client_data_01, client_data_02, client_data_03])

# menuuuuuuu
initial_menu = ["Staff Menu", "Help Desk Menu", "Print Tickets", "Display Ticket Statistics"]
help_desk_menu = ["Resolve", "Reopen", "Respond"]
staff_menu = ["Submit a Ticket"]

while True:
    print("\n<<<<<<--Help Desk Ticketing System Prototype!-->>>>>")
    section_choice = menuload(initial_menu)

    # EXIT
    if section_choice == 0:
        print("Goodbye!")
        break

    # Staff Menu
    elif section_choice == 1:
        staff_menu_choice = menuload(staff_menu)

        if staff_menu_choice == 1:
            submit_ticket()

            for ticket in client_list:
                if contains_password_reset_keyword(ticket):
                    ticket.ticket_status = "Closed"
                    new_password = generate_new_password()
                    ticket.response = f"New Password: {new_password}"

        elif staff_menu_choice == 0:
            print("Going back to Main Menu")
            continue

    # Help Desk Menu
    elif section_choice == 2:
        ticket_edit()

    # Printing Tickets
    elif section_choice == 3:
        print("\nPrinting Tickets: ")
        for x in client_list:
            print(x)

        """ 
        print_choice = int(input("print 1 or print 2: "))
        if print_choice == 1:
            print_tickets_choice = printing_tickets()

            if print_tickets_choice == 0:
                print("Going back to Main Menu...")
                continue
                
        elif print_choice == 2:
        """

    # Display Ticketing Statistics
    elif section_choice == 4:
        section_choice = display_ticket_statistics()

    else:
        continue
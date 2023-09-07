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

        # why does it consider the count as a parameter? how does it work?
        if choice in range(0, count):
            answer = choice

        else:
            print("Error: Number out of RANGE.")
            answer = 99

    else:
        print("Error: Input NOT a number.")
        answer = 99

    return answer


# --------------------<< PRINTING TICKETS >>--------------------
def printing_tickets():
    found = 0
    vTemp = []

    for v in client_list:
        if v.vStatus == True:
            vTemp.append(f"Ticket Number: {Ticket.ticket_number}\n"
                         f"Ticket creator: {v.ticket_creator}\n"
                         f"Staff ID: {v.staff_id}\n"
                         f"Email Address: {v.email}\n"
                         f"Description: {v.desc}\n"
                         f"Response: {v.response}\n"
                         f"Ticket Status: {v.ticket_status}\n")

    test = menuload(vTemp)

    if test != 0:
        found = client_list[test - 1]

    return found
# --------------------<< class >>--------------------


from Tickets import Ticket

client_list = []
# --------------------<< main >>--------------------
client_data_01 = Ticket("Inna", "INNAM", "inna@whitecliffe.co.nz", "My monitor stopped working", "Not Yet Provided", "Open")
client_data_02 = Ticket("Maria", "MARIAH", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars", "Not Yet Provided", "Open")
client_data_03 = Ticket("John", "JOHNS", "john@whitecliffe.co.nz", "Password change", "New password generated: JOJoh", "Closed")
client_list.extend([client_data_01, client_data_02, client_data_03])

initial_menu = ["Customer Menu", "Help Desk Menu", "Printing Tickets", "Display Ticket Statistics"]
help_desk_menu = []
customer_menu = []
while True:
    print("<<<<<<Help Desk Ticketing System Prototype!>>>>>\n")
    section_choice = menuload(initial_menu)

    if section_choice == 0:
        print("Goodbye!")
        break

    elif section_choice == 1: # Customer Menu
        customer = menuload(customer_menu)

    elif section_choice == 2: # Help Desk Menu
        help_desk = menuload(help_desk_menu)

    elif section_choice == 3: # Printing Tickets
        print_tickets_choice = printing_tickets()

        if print_tickets_choice == 0:
            print("Goodbye -- print_tickets_choice")
            break

    elif section_choice == 4: # Display Ticketing Statistics
        section_choice = menuload()

    else:
        continue
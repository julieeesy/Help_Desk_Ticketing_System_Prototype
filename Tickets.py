import itertools

class Ticket:
    id_object = itertools.count(2000)

    # The task of constructors is to initialize(assign values) to
    # the data members of the class when an object of the class is created.
    def __init__(self, ticket_creator, staff_id, email, desc): # https://realpython.com/python-multiple-constructors/#using-optional-argument-values-in-__init__
        self.ticket_number = next(Ticket.id_object) # https://bobbyhadz.com/blog/python-create-incremental-id-in-class
        self.ticket_creator = ticket_creator
        self.staff_id = staff_id
        self.email = email
        self.desc = desc
        self.response = "Not Yet Responded"
        self.ticket_status = "Open"
        self.Status = True # https://realpython.com/python-class-constructor/    ||    https://realpython.com/python-optional-arguments/

    def __str__(self): # https://realpython.com/python-repr-vs-str/
        return (f"Ticket Number: {self.ticket_number}\n"
                f"Ticket creator: {self.ticket_creator}\n"
                f"Staff ID: {self.staff_id}\n"
                f"Email: {self.email}\n"
                f"Description: {self.desc}\n"
                f"Response: {self.response}\n"
                f"Ticket status: {self.ticket_status}\n")

    def new_response(self):
        new_resp = input("Enter New RESPONSE: ")
        self.response = new_resp

    def new_ticket_status(self):
        new_status = input("Enter New TICKET STATUS [open/closed]: ")
        self.ticket_status = new_status

